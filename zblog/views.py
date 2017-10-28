from django.shortcuts import render
#...from 다음에 있는 마침표(.)는 현재 디렉토리 또는 애플리케이션을 의미합니다.
from .models import Zpost
from django.utils import timezone

# Create your views here.
def post_list(request):
    #return render(request, 'post_list.html')
    #return render(request, 'zblog/post_list.html', {})
    posts = Zpost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'zblog/post_list.html', {'posts': posts})
