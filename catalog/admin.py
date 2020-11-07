from django.contrib import admin
from . import models


class BooksInstanceInline(admin.TabularInline):
    pass


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
