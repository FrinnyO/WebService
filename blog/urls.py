from django.urls import path

from .views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView

urlpatterns = [
    path("articles_list/", ArticleListView.as_view(), name="articles_list"),
    path("article_create/", ArticleCreateView.as_view(), name="article_create"),
    path("article_detail/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("article_update/<int:pk>/", ArticleUpdateView.as_view(), name="article_update"),
    path("article_confirm_delete/<int:pk>/", ArticleDeleteView.as_view(), name="article_delete"),
]
