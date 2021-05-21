from django.contrib import admin
from books.models import Book
from books.models import BookUser

admin.site.register(Book)
admin.site.register(BookUser)
