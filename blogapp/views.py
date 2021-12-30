from django.shortcuts import get_object_or_404, render
from .models import Post


# Create your views here.
def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3] 
    return render(request,'app/index.html',{
        "posts":latest_posts
    })

def posts(request):
    all_posts=Post.objects.all().order_by("-date")
    return render(request,"app/allpost.html",{"all_posts":all_posts})

def post_details(request,slug):
        identified_post=get_object_or_404(Post,slug=slug)
        return render(request,"app/post-details.html",{"post":identified_post})
    