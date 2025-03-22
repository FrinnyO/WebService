from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.models import Category, Contact, Product

from .forms import ProductForm

ALL_CATEGORIES = Category.objects.all()


def contacts(request):
    return render(request, "catalog/contacts.html")


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get(self, request):
        all_products = Product.objects.all()
        paginator = Paginator(all_products, 4)

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
    success_url = reverse_lazy("home")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("home")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = "product"
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("home")
