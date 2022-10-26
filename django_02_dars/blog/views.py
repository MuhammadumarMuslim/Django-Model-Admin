from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Author
from .models import Author

def author_list(request):
    authors = Author.objects.all()
    print(authors)
    author_list = ""
    for author in authors:
        author_list += f"<li>{author.first_name} {author.last_name}</li>"
    return HttpResponse(f"<ul>{author_list}</ul>")
