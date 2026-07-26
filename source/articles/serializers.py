from rest_framework import serializers

from articles.models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'status', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']


class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'article', 'text', 'author', 'created_at']
        read_only_fields = ['author', 'article', 'created_at']


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'article', 'text', 'author', 'created_at']
        read_only_fields = ['author', 'article', 'created_at']
        extra_kwargs = {
            'text': {'required': True}
        }