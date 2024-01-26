from django.db import models

from apps.common.models import BaseModel


class Author(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/images/')
    description = models.TextField()

    is_top = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class SocialNetwork(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='social_networks/')

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='socials')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SocialNetwork'
        verbose_name_plural = 'SocialNetworks'
