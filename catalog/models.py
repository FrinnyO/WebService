from django.db import models
from mypy.main import maybe_write_junit_xml


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Введите название категории")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Введите название продукта")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="products", blank=True, null=True, verbose_name="Изображение", default="placeholder.png"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.FloatField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]


class Contact(models.Model):
    country = models.CharField(max_length=100, verbose_name="Страна")
    individual_number = models.CharField(max_length=100, verbose_name="ИНН")
    address = models.TextField(verbose_name="Адрес")

    def __str__(self):
        return f"{self.country} {self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["country", "address"]
