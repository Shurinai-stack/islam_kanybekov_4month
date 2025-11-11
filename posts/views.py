from django.shortcuts import render,HttpResponse, redirect 
from posts.models import Post
from posts.forms import PostForm

def home_view(request):
    if request.method == "GET":
        return render(request, "base.html")

def test_view(request):
    return HttpResponse("Криштиану Роналду Душ Сантос Авейру")

def view_html(request):
    if request.method == "GET ":
        return render(request, "base.html")

def posts_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/posts_list.html", context={"posts":posts})

def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post":post})
    
def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render (request, "posts/post_create.html", context={"form":form})
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request,"posts/post_create.html", context={"form":form})
        
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        rate = form.cleaned_data["rate"]
        image = form.cleaned_data["image"]

        try:
            post = Post.objects.create(title=title, content=content, rate=rate, image=image)
            return redirect("/posts")
        except Exception as e:
            return HttpResponse(f"Error: {e}")