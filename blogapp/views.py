from django.shortcuts import render
from datetime import date

all_posts=[
    {
        "image":"mountains.jpg",
        "slug":"hike-in-the-mountains",
        "author":"Partha",
        "date": date(2021,11,5),
        "title":"Mountain Hiking",
        "excerpt":"There is nothing like the view you get when hiking the mountain!",
        "content": """
                    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas consequuntur suscipit 
        voluptas doloremque mollitia dignissimos sint aut voluptate reiciendis. Atque, recusandae vero
         ducimus totam nam perferendis. Ea expedita doloremque doloribus!

         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas consequuntur suscipit 
        voluptas doloremque mollitia dignissimos sint aut voluptate reiciendis. Atque, recusandae vero
         ducimus totam nam perferendis. Ea expedita doloremque doloribus!

         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas consequuntur suscipit 
        voluptas doloremque mollitia dignissimos sint aut voluptate reiciendis. Atque, recusandae vero
         ducimus totam nam perferendis. Ea expedita doloremque doloribus!
        """
    },

     {  
        "image":"coding.jpg",
        "slug":"programming-is-fun",
        "author":"Partha",
        "date": date(2021,10,7),
        "title":"Programming is great",
        "excerpt":"Did you spent hours and hours of time for finding a single error in your code??",
        "content": """
                    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas consequuntur suscipit 
        voluptas doloremque mollitia dignissimos sint aut voluptate reiciendis. Atque, recusandae vero
         ducimus totam nam perferendis. Ea expedita doloremque doloribus!

         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas consequuntur suscipit 
        voluptas doloremque mollitia dignissimos sint aut voluptate reiciendis. Atque, recusandae vero
         ducimus totam nam perferendis. Ea expedita doloremque doloribus!

         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas consequuntur suscipit 
        voluptas doloremque mollitia dignissimos sint aut voluptate reiciendis. Atque, recusandae vero
         ducimus totam nam perferendis. Ea expedita doloremque doloribus!
        """
    },

     {
        "image":"woods.jpg",
        "slug":"into-the-woods",
        "author":"Partha",
        "date": date(2021,9,15),
        "title":"Nuture at it's best",
        "excerpt":"Nature is amazing. I getrid of everything while walking through by woods",
        "content": """
                    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas consequuntur suscipit 
        voluptas doloremque mollitia dignissimos sint aut voluptate reiciendis. Atque, recusandae vero
         ducimus totam nam perferendis. Ea expedita doloremque doloribus!

         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas consequuntur suscipit 
        voluptas doloremque mollitia dignissimos sint aut voluptate reiciendis. Atque, recusandae vero
         ducimus totam nam perferendis. Ea expedita doloremque doloribus!

         Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas consequuntur suscipit 
        voluptas doloremque mollitia dignissimos sint aut voluptate reiciendis. Atque, recusandae vero
         ducimus totam nam perferendis. Ea expedita doloremque doloribus!
        """
    },
]

# to get post date
def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-2:]
    return render(request,'app/index.html',{
        "posts":latest_posts
    })

def post(request):
    return render(request,"app/allpost.html",{"all_posts":all_posts})

def post_details(request,slug):
    identified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request,"app/post-details.html",{"post":identified_post})
