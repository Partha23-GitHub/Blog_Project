from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from.models import Post,Author,Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter=("author","tags",'date')
    list_display=("date","title","author")

class AuthorFilter(admin.ModelAdmin):
    List_filter=("email_address")    

admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorFilter)
admin.site.register(Tag)