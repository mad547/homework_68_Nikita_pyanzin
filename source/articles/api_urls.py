from django.urls import path
from articles.api_views import (
    ArticleListView,
    ArticleDetailView,
    CommentListView,
    CommentDetailView,
)

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='api-article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='api-article-detail'),
    path('articles/<int:article_pk>/comments/', CommentListView.as_view(), name='api-comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='api-comment-detail'),
]