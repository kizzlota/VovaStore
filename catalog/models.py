from django.db import models
from django.contrib import admin
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "author"]
    search_fields = ["title", "text", "author"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
