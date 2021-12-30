from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email_address=models.EmailField()
    def __str__(self): 
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption=models.CharField(max_length=25)
    def __str__(self): 
        return f"{self.caption}"

class Post(models.Model):
    title=models.CharField(max_length=40)
    excerpt=models.CharField(max_length=50)
    image_name=models.CharField(max_length=20)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True)
    content=models.TextField(max_length=2000,validators=[MinLengthValidator(15)])
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    tags=models.ManyToManyField(Tag)

