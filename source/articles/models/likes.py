from django.contrib.auth import get_user_model
from django.db import models

from articles.models.base_model import BaseModel


class ArticleLike(BaseModel):
    article = models.ForeignKey(
        'articles.Article',
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Статья'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='article_likes',
        verbose_name='Пользователь'
    )

    class Meta:
        db_table = 'article_like'
        verbose_name = 'Лайк статьи'
        verbose_name_plural = 'Лайки статей'
        unique_together = ('article', 'user')

    def __str__(self):
        return f'{self.user} лайкнул {self.article}'


class CommentLike(BaseModel):
    comment = models.ForeignKey(
        'articles.Comment',
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Комментарий'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comment_likes',
        verbose_name='Пользователь'
    )

    class Meta:
        db_table = 'comment_like'
        verbose_name = 'Лайк комментария'
        verbose_name_plural = 'Лайки комментариев'
        unique_together = ('comment', 'user')

    def __str__(self):
        return f'{self.user} лайкнул {self.comment}'