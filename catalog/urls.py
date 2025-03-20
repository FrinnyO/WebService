from django.urls import path

from . import views

urlpatterns = [
    path("contacts/", views.contacts, name="contacts"),
    path("home/", views.home, name="home"),
    path("product/<int:pk>/", views.single_product, name="single_product"),
    path("add_product/", views.add_product, name="add_product"),
]
