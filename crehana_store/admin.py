from django.contrib import admin

from .models import Category, Course, Subcategory

# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Subcategory)
