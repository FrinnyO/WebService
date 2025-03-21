from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="articles", blank=True, null=True, verbose_name="Изображение", default="placeholder.png")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата Создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    views_counter = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ["views_counter", "title"]