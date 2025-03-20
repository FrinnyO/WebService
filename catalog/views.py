from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Contact, Category, Product

ALL_CATEGORIES = Category.objects.all()

def contacts(request):
    return render(request, "catalog/contacts.html")


def home(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 4)  # Show 4 products per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "categories": ALL_CATEGORIES}
    return render(request, "catalog/home.html", context)


def contacts(request):
    all_contacts = Contact.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"""Спасибо, {name}! 
        Мы получили ваше сообщение: ({message}).
        Мы перезвоним вам по телефону: {phone}"""
        )
    context = {"categories": ALL_CATEGORIES, "contacts": all_contacts}

    return render(request, "catalog/contacts.html", context)


def single_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {"categories": ALL_CATEGORIES, "product": product}

    return render(request, "catalog/single_product.html", context)


def add_product(request):
    categories = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_name = request.POST.get("category")
        image = request.FILES.get("image")

        category = Category.objects.get(name=category_name)

        print(image)

        Product.objects.create(name=name, description=description, price=price, category_id=category.pk, image=image)

        return HttpResponse("Продукт успешно добавлен")

    return render(request, "catalog/add_product.html", {"categories": categories})
