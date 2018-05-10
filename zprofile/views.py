from django.shortcuts import render

# Create your views here.
def home(request):
    #return render(request, 'post_list.html')
    #return render(request, 'zblog/post_list.html', {})
    #posts = Zpost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'zprofile/home.html', {})


def home_en(request):
    #pass
    # request.POST, request.FILES
    return render(request, 'zprofile/home_en.html', {})

def home_hmd(request):
    #pass
    # request.POST, request.FILES
    return render(request, 'zprofile/home_hmd.html', {})
