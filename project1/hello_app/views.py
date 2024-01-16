from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    movie_data={'movies':[{
        'title':'God father',
        'year':1990,
        'summary': 'story of an underworld kin',
        'success':False
    },
    {
        'title':'Life of pi',
        'summary': 'story of an Tiger',
        'success':False
    },
    {
        'title':'Life lesson',
        'year':2004,
        'summary': 'story of an life',
        'success':False
    }]}
    return render(request,"hello.html",movie_data)

