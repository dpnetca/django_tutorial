from django.shortcuts import render

# Create your views here.

posts = [
    {
        "author": "dpnetca",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": " August 15, 2019",
    },
    {
        "author": "dpnetca",
        "title": "Blog Post 2",
        "content": "Seecond post content",
        "date_posted": " August 15, 2019",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
