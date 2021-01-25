from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
    'title': 'Página inicial',
    'content': 'Bem-vindo a página inicial'
    }    
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
    'title': 'Página sobre',
    'content': 'Bem-vindo a página sobre'
    }
    return render(request, 'about/view.html', context)

def contact_page(request):
    context = {
    'title': 'Página de contato',
    'content': 'Bem-vindo a página contatos'
    }
    if request.method == "POST":
        print(request.POST)
    
    return render(request, 'contact/view.html', context)