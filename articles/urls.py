from . views import ArticleDetailView
from django.urls import path

urlpatterns = [
    path('', ArticleDetailView.as_view(), name="article_detail"),
]
