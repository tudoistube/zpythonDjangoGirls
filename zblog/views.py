#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
#...from 다음에 있는 마침표(.)는 현재 디렉토리 또는 애플리케이션을 의미합니다.
from .models import Zpost
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    #return render(request, 'post_list.html')
    #return render(request, 'zblog/post_list.html', {})
    posts = Zpost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'zblog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Zpost, pk=pk)
    return render(request, 'zblog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'zblog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'zblog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Zpost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'zblog/post_edit.html', {'form': form})
