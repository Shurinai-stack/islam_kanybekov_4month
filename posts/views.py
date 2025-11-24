from django.shortcuts import render,HttpResponse, redirect 
from posts.models import Post
from posts.forms import PostForm, SearchForm, PostForm2
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, CreateView



class TestView(View):
    def get(self, request):
        return HttpResponse("Hello world!")


def home_view(request):
    if request.method == "GET":
        return render(request, "base.html")

def test_view(request):
    return HttpResponse("Криштиану Роналду Душ Сантос Авейру")

def view_html(request):
    if request.method == "GET ":
        return render(request, "base.html")

@login_required(login_url='/login/')
def posts_list_view(request):
    posts = Post.objects.all()
    form = SearchForm()
    limit = 3

    if request.method == "GET":
        query_params = request.GET
        search = query_params.get("search")
        category_id = query_params.get("category_id")
        tags_ids = query_params.getlist("tags_ids")
        ordering = query_params.get('ordering')
        page = int(query_params.get("page", 1))

        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))

        if category_id:
            posts = posts.filter(category_id=category_id)

        if tags_ids:
            posts = posts.filter(tags__id__in=tags_ids).distinct()

        if ordering:
            posts = posts.order_by(ordering)

        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages + 1)
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]

        return render(
            request,
            "posts/posts_list.html",
            context={
                "posts": posts,
                "form": form,
                "pages": range(1, max_pages + 1)
            }
        )

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm2
    template_name = 'posts/post_create.html'
    success_url = '/posts/'

@login_required(login_url='/login/')
def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post":post})

@login_required(login_url='/login/')
def post_create_view(request):
    if request.method == "GET":
        form = PostForm2()
        return render (request, "posts/post_create.html", context={"form":form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request,"posts/post_create.html", context={"form":form})
        
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        rate = form.cleaned_data["rate"]
        image = form.cleaned_data["image"]

        try:
            # post = Post.objects.create(title=title, content=content, rate=rate, image=image)
            form.save()
            return redirect("/posts")
        except Exception as e:
            return HttpResponse(f"Error: {e}")

@login_required(login_url='/login/')    
def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id, author=request.user)
    if request.method == 'GET':
        form = PostForm2(instance=post)
        return render(request, 'posts/post_update.html', context={'form':form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, 'posts/post_update.html', context={"post":post})
        form.save()
        return redirect("/profile/")