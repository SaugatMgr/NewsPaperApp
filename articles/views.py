from django.views.generic import ListView
from .models import Article

class ArticleDetailView(ListView):
    model = Article
    template_name = "article_list.html"