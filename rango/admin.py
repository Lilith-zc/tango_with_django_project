from django.contrib import admin
from rango.models import Category, Page

class Pagelist(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class Categorylist(admin.ModelAdmin):
    list_display = ('name','views','likes')

admin.site.register(Category, Categorylist)
admin.site.register(Page, Pagelist)

