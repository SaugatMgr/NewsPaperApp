from django.views.generic import ListView
from .models import Article

class ArticleDetailView(ListView):
    model = Article
    template = "article_list.html"