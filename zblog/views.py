from django.shortcuts import render

# Create your views here.
def post_list(request):
    #return render(request, 'post_list.html')
    return render(request, 'zblog/post_list.html', {})
