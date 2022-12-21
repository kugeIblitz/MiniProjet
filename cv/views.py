from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio,Experience

def index(request):

    home=Home.objects.latest('updated')

    about=About.objects.latest('updated')

    profiles=Profile.objects.filter(about=about)

    categories=Category.objects.all()
    experience=Experience.objects.all()
    
    portfolio=Portfolio.objects.all()
  
    context={
        'home':home,
        'about':about,
        'profiles':profiles,
        'categories':categories,
        'experience':experience,
        'portfolio':portfolio,
    }
    return render(request,'index.html',context)

