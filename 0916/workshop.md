```python
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm

# Create your views here.
def user_list(request):
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/user_list.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:user_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_list')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def profile(request, username):
    # user = get_user_model().objects.get()
    User = get_user_model()
    user = User.objects.get(username=username)
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('accounts:user_list')


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:user_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            ##### get_user의 역할이 무엇인지
            auth_login(request, form.get_user())
            return redirect('accounts:user_list')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_list')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def password(request):
    if request.method == 'POST':
        ###### 왜 request.user넣는지
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)
```

