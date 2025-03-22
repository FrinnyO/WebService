from django.urls import path

from .views import (ContactsView, HomeListView, ProductCreateView, ProductDeleteView, ProductDetailView,
                    ProductUpdateView)

urlpatterns = [
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("home/", HomeListView.as_view(), name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="single_product"),
    path("add_product/", ProductCreateView.as_view(), name="add_product"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
