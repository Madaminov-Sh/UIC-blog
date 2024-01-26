from django.db import models

from apps.common.models import BaseModel
from apps.authors.models import Author


class Post(BaseModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='posts/images')
    content = models.TextField()

    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Category(BaseModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories/images')

    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(BaseModel):
    title = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
