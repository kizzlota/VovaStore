from django.shortcuts import render
from models import Post
# Create your views here.
def index(request):
    category = request.GET.get('c', 'levis')
    posts = Post.objects.filter( author__name = category ).order_by( '-id' )

    return render(request, 'catalog/index.html', {'posts': posts})