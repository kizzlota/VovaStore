from django.db import models
from django.contrib import admin
# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __unicode__(self):
		return self.name


class CategoryAdmin(admin.ModelAdmin):
	list_display = ["name", "description"]
	search_fields = ["name"]


class Shoes(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(blank=True, null=True, upload_to='shoes_images', default="/static/img/shoesimage.jpg")
	price = models.IntegerField()
	decription = models.CharField(max_length=150, blank=True, null=True)
	category_name = models.ForeignKey(Category)


class ShoesAdmin(admin.ModelAdmin):
	list_display = ["name", "price", "category_name"]
	search_fields = ["name", "price", "category_name"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Shoes, ShoesAdmin)

