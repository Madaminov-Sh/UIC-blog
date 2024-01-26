from rest_framework import serializers

from .models import ContactUs


class ContactUstSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('id', 'name', 'subject', 'email', 'text', 'created_at', 'updated_at')

