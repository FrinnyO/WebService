from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "views_counter", "created_at", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title",)
