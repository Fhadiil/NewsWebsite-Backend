from django.contrib import admin
from .models import Article, Advertisement, Category, Comment, CustomUser

admin.site.register(Article)
admin.site.register(Advertisement)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(CustomUser)


