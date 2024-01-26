from rest_framework import serializers

from .models import Post, Category, Tag
from apps.authors.serializers import AuthorSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'image',  'count')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'title', 'category')


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'category', 'author', 'created_at', 'updated_at')
