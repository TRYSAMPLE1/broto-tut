from django.shortcuts import render
from . models import MovieInfo

# Create your views here.

def create(request):
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        desc=request.POST.get('summary')
        movie_obj=MovieInfo(title=title,year=year,description=desc)
        movie_obj.save()


    return render(request,'create.html')

def list(request):
    movie_data=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_data})

def edit(request):
    return render(request,'edit.html')