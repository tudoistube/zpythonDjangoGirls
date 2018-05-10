from django.shortcuts import render

# Create your views here.
def profile_list(request):
    #return render(request, 'post_list.html')
    #return render(request, 'zblog/post_list.html', {})
    #posts = Zpost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'zprofile/profile_list.html', {})
