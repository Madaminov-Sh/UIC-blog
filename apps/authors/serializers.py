from rest_framework import serializers

from .models import Author, SocialNetwork


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ('id', 'title', 'image')


class AuthorSerializer(serializers.ModelSerializer):
    socials = SocialNetworkSerializer(many=True)

    class Meta:
        model = Author
        fields = ('id', 'title', 'description', 'image', 'socials', 'is_top')
