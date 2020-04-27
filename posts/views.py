from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Post

def posts_create(request):
    """Logic to handle requests and return responses."""
    context_data = {"title": "Create"}#
    return render(request, "index.html", context_data)
    #return HttpResponse("<h1>Create<h1>")

def posts_detail(request, id):
    """Logic to handle requests and return responses."""
    instance = get_object_or_404(Post, id=id)
    context_data = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_details.html", context_data)
    #return HttpResponse("<h1>Detail<h1>")

def posts_list(request):
    """Logic to handle requests and return responses."""
    queryset = Post.objects.all()
    context_data = {
        "title": "Posts",
        "object_list": queryset
    }
    return render(request, "posts_list.html", context_data)
    #return HttpResponse("<h1>List<h1>")

def posts_update(request):
    """Logic to handle requests and return responses."""
    context_data = {"title": "Update"}#
    return render(request, "index.html", context_data)
    #return HttpResponse("<h1>Update<h1>")

def posts_delete(request):
    """Logic to handle requests and return responses."""
    context_data = {"title": "Delete"}#
    return render(request, "index.html", context_data)
    #return HttpResponse("<h1>Delete<h1>")
