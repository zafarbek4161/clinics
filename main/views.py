from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def home(request):
    return render(request,'main/home.html')
    
def about(request):
    return render(request, 'main/about.html')

def consultation(request):
    return render(request, 'main/consultation.html')

def contact(request):
    return render(request, 'main/contact.html')