from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','text', 'created_date', 'published_date')
# Register your models here.
