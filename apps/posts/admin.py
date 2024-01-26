from django.contrib import admin
# from django.apps import apps

from .models import Post, Category, Tag

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except:
#         pass


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
