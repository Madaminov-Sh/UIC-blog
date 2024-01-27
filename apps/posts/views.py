from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import PostSerializer, CategorySerializer, TagSerializer
from .models import Post, Category, Tag


class PostsListsView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostPopularApiView(ListAPIView):
    queryset = Post.objects.filter(is_popular=True).order_by("?")[:8]
    serializer_class = PostSerializer


class PostRecentlyApiView(ListAPIView):
    queryset = Post.objects.filter().order_by('-published_date')
    serializer_class = PostSerializer


class PostDetailApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoriesListsView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TagsListsView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
