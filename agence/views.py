from django.shortcuts import render
from django.shortcuts import redirect


#  for the home page 
def index(request):
    return render(request, template_name ='pages/index.html',)

# for the informations page (about)
def about(request):
    return render(request, template_name ='pages/about.html',)

# for the services page
def service(request):
    return render(request, template_name='pages/services.html',)

# for the catalogue page
def catalogue(request):
    return render(request, template_name='pages/catalogue.html',)

# for the contact page
def contact(request):
    return render(request, template_name='pages/contact.html',)