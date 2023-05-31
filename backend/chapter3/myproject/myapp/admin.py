from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
   list_display = ['title', 'author', 'publication_date', 'price']
   search_fields = ['title', 'author']
   list_filter = ['author', 'publication_date']