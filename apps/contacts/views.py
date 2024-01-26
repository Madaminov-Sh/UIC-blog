from rest_framework.generics import CreateAPIView

from .models import ContactUs
from .serializers import ContactUstSerializer


class ContactUsApiView(CreateAPIView):
    queryset = ContactUs
    serializer_class = ContactUstSerializer
