from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


class Bookinline(admin.TabularInline):
    pass


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "date_of_birth",
        "date_of_death",
    )
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "due_back", "id")
    list_filter = ("status", "due_back")
    fieldsets = (
        (None, {"fields": ("book", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back")}),
    )


# admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)