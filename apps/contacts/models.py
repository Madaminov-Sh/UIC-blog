from django.db import models

from apps.common.models import BaseModel


class ContactUs(BaseModel):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
