from django.contrib import admin

# Register your models here.
from .models import BlogPost, Tag


admin.site.register(Tag)
admin.site.register(BlogPost)
