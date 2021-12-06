
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from . forms import movieform

from movieapp.models import MOVIE

# Create your views here.

def movie(request):
    movie=MOVIE.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def details(request,movie_id):
    movie=MOVIE.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})

def add_movie(request):
    if request.method=='POST':
        nm=request.POST.get('name')
        yr=request.POST.get('year')
        disc=request.POST.get('disc')
        image=request.FILES['image']
        movie=MOVIE(name=nm,disc=disc,year=yr,img=image)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie=MOVIE.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=MOVIE.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')