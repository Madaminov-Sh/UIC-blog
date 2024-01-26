from rest_framework.generics import ListAPIView

from .serializers import PostSerializer, CategorySerializer, TagSerializer
from .models import Post, Category, Tag


class PostsListsView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CategoriesListsView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TagsListsView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
