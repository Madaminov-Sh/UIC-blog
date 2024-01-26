from rest_framework.generics import ListAPIView

from .serializers import AuthorSerializer
from .models import Author


class AuthorsListsApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer