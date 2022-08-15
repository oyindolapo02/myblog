from django.shortcuts import render


def home(request):
    return render(request, 'Home.html')


def article(request):
    return render(request, 'Article.html')


def team(request):
    return render(request, 'Team.html')

def contact(request):
    return render(request, 'Contact.html')

# Create your views here.
