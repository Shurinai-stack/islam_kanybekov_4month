from django.shortcuts import render,HttpResponse
from posts.models import Post

def home_view(request):
    return render(request, "base.html")

def test_view(request):
    return HttpResponse("Криштиану Роналду Душ Сантос Авейру")

def view_html(request):
    return render(request, "base.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", context={"posts":posts})