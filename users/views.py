from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from users.forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout

def register_view(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'users/register.html', context={'form': form})
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            return redirect('/')
        
        try:
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
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
    
def logout_view(request):
    logout(request)
    return redirect ('/')
    