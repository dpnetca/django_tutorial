from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Book, Author, BookInstance, Genre


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(
        status__exact="a"
    ).count()
    num_authors = Author.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    # genre_word = "war"
    # book_word = "red"
    # num_genre_contain_word = Genre.objects.filter(
    #     name__contains=genre_word
    # ).count()
    # num_book_contain_word = Book.objects.filter(
    #     title__contains=book_word
    # ).count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_visits": num_visits,
        # "num_genre_contain_word": num_genre_contain_word,
        # "num_book_contain_word": num_book_contain_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "catalog\index.html", context=context)
