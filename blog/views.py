from django.shortcuts import render
from blog.models import Post

# Create your views here.

post = [
    {
        'author' : 'Arun',
        'title' : "First Dictionary",
        'date' : 'January 16, 2020'
    },
    {
        'author' : 'Ghimire',
        'title' : "Second Dictionary",
        'date' : '16 January, 2020'
    }
#This data when passed to the templates is not static.
#We will not pass this data to the templates. This Dictionary is created only for understanding purpose.
#We have passed the dynamic data in the below view functions

]

def home(request):
    context = {'posts':Post.objects.all()}
    #Here the posts keyword consists of all the Posts created by the users themselves using the 'Post' class in models.py
    #This is now the DYNAMIC DATA that is passed to the templates
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title':'About'})
