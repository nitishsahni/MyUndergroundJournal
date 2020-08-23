from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.shortcuts import render, redirect
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'entry')


def signup(request):
    if request.user.is_authenticated:
        return redirect('entries')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('login')

#########################

@login_required(login_url='signup')
def entries(request):
    entries = Post.objects.filter(user=request.user).order_by('-pk')
    context = {'entries': entries}
    return render(request, 'entries.html', context)

@login_required(login_url='signup')
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('entries')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})