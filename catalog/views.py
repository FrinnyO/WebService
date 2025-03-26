from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from catalog.models import Category, Contact, Product

from .forms import ProductForm

ALL_CATEGORIES = Category.objects.all()


def contacts(request):
    return render(request, "catalog/contacts.html")


class HomeListView(ListView):
    model = Product
    context_object_name = "products"

    def get(self, request):
        published_products = Product.objects.filter(is_published=True)
        paginator = Paginator(published_products, 4)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {"products": page_obj, "categories": ALL_CATEGORIES}
        return render(request, "catalog/home.html", context)


class ContactsView(TemplateView):
    model = Contact
    template_name = "catalog/contacts.html"

    def get(self, request):
        all_contacts = Contact.objects.all()
        context = {"categories": ALL_CATEGORIES, "contacts": all_contacts}

        return render(request, "catalog/contacts.html", context)

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"""Спасибо, {name}! 
        Мы получили ваше сообщение: ({message}).
        Мы перезвоним вам по телефону: {phone}"""
        )


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/single_product.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        if form.instance.owner == self.request.user:
            return super().form_valid(form)
        return HttpResponseForbidden("У вас нет прав доступа для редактирования продукта")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    permission_required = "products.delete_product"
    model = Product
    context_object_name = "product"
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        if not request.user.has_perm("delete_product") and not request.user == product.owner:
            return HttpResponseForbidden("У вас нет прав на удаление продукта!")
        product.delete()
        return redirect("catalog:home")


class UnpublishedProductsListView(ListView):
    model = Product
    context_object_name = "products"

    def get(self, request):
        unpublished_products = Product.objects.filter(is_published=False)
        paginator = Paginator(unpublished_products, 4)  # Show 4 products per page

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {"products": page_obj, "categories": ALL_CATEGORIES}
        return render(request, "catalog/home.html", context)


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm("products.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав на снятие товара с публикации")

        product.is_published = False if product.is_published else True
        product.save()
        return redirect("catalog:home")
