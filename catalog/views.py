from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"""Спасибо, {name}! 
        Мы получили ваше сообщение: ({message}).
        Мы перезвоним вам по телефону: {phone}""")
    return render(request, 'catalog/contacts.html')