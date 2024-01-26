from django.contrib import admin

from .models import Author, SocialNetwork


class AuthorInline(admin.StackedInline):
    model = SocialNetwork


class AuthorAdmin(admin.ModelAdmin):
    inlines = [AuthorInline]


admin.site.register(Author, AuthorAdmin)
admin.site.register(SocialNetwork)
