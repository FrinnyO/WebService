from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "обман",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["created_at", "updated_at", "is_published", "owner"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название продукта"})
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )
        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите изображение продукта"}
        )

        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите категорию продукта"}
        )
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите цену продукта"})

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(word in name.lower() for word in FORBIDDEN_WORDS):
            raise ValidationError("Название содержит запрещенные слова")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if any(word in description.lower() for word in FORBIDDEN_WORDS):
            raise ValidationError("Описание содержит запрещенные слова")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Размер изображения не должен превышать 5 Мб")

            if hasattr(image.file, "content_type") and image.file.content_type not in ["image/jpeg", "image/png"]:
                raise ValidationError("Формат изображения должен быть JPEG или PNG")
        return image
