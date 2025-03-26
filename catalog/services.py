from django.core.cache import cache

from config.settings import CACHE_ENABLED

from .models import Category, Product


class ProductService:

    @staticmethod
    def get_products_in_category(category_id):
        if not CACHE_ENABLED:
            return Product.objects.filter(category_id=category_id)
        key = "products_in_category"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products, 60 * 15)
        return products

    @staticmethod
    def get_all_categories():
        if not CACHE_ENABLED:
            return Category.objects.all()
        key = "all_categories"
        categories = cache.get(key)
        if categories is not None:
            return categories
        categories = Category.objects.all()
        cache.set(key, categories, 60 * 15)
        return categories
