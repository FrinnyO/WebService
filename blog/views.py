from django.shortcuts import render

from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Article
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class ArticleListView(ListView):
    model = Article
    template_name = "blog/articles_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(is_published=True)

    def get(self, request):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 4)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {"articles": page_obj}
        return render(request, "blog/articles_list.html", context)


class ArticleCreateView(CreateView):
    model = Article
    template_name = "blog/article_create.html"
    context_object_name = "article"
    fields = ["title", "content", "preview"]
    success_url = reverse_lazy("articles_list")


    def form_valid(self, form):
        form.instance.is_published = True
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def get_object(self, queryset=None):
        article = super().get_object(queryset)
        article.views_counter += 1
        article.save()
        return article


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "blog/article_update.html"
    fields = ["title", "content", "preview", "is_published"]

    def get_success_url(self):
        return reverse_lazy("article_detail", kwargs={"pk": self.object.pk})

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("articles_list")