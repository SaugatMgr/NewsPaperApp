from . views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
)

from django.urls import path

urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('new/', ArticleCreateView.as_view(), name="article_create"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),    
]
