from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from users.forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from users.models import Profile
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.forms import PostForm

def register_view(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'users/register.html', context={'form': form})
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if not form.is_valid():
            return redirect('/')
        
        try:
            form.cleaned_data.__delitem__('password_confirm')
            age = form.cleaned_data.pop('age')
            image = form.cleaned_data.pop('image')
            user = User.objects.create_user(
                **form.cleaned_data
            )
            if user:
                Profile.objects.create(user=user, age=age, image=image)
            return redirect('/')
        except Exception as e:
            return HttpResponse(f'Error: {e}')
        
def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'users/login.html', context={'form': form})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/login.html', context={'form': form})
        
        user = authenticate(**form.cleaned_data)
        if not user:
            form.add_error(None, 'Invalid username or password')
            return render(request, 'users/login.html', context={'form': form})
        login(request, user)
        return redirect('/')
    
@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect ('/')

@login_required(login_url='/login/')    
def profile_view(request):
    if request.method == 'GET':
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
            posts = Post.objects.filter(author=user)
        except Exception:
            return HttpResponse('No profile found')
        return render(request, 'users/profile.html', context={'profile': profile, 'posts': posts})


