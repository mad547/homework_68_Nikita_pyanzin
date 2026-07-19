from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from articles.models import Article, Comment, ArticleLike, CommentLike


@login_required
@require_http_methods(["POST"])
def article_like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    like, created = ArticleLike.objects.get_or_create(
        article=article,
        user=request.user
    )
    if created:
        article.likes_count += 1
        article.save()
        liked = True
    else:
        like.delete()
        article.likes_count -= 1
        article.save()
        liked = False

    return JsonResponse({
        'likes_count': article.likes_count,
        'liked': liked
    })


@login_required
@require_http_methods(["POST"])
def comment_like(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    like, created = CommentLike.objects.get_or_create(
        comment=comment,
        user=request.user
    )
    if created:
        comment.likes_count += 1
        comment.save()
        liked = True
    else:
        like.delete()
        comment.likes_count -= 1
        comment.save()
        liked = False

    return JsonResponse({
        'likes_count': comment.likes_count,
        'liked': liked
    })