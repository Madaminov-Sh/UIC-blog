from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import AuthorSerializer
from .models import Author


class AuthorsListsApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailApiView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
