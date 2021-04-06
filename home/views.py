from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {
        "variable1":"Hi Anmol?",
        "variable2":"Hello! How are you."
    }
   # return HttpResponse("this is home page")
    return render(request, "home.html", context) 

def about(request):
     return render(request, "about.html") 

def services(request):
     return render(request, "services.html") 

def contact(request):
     return render(request, "contact.html") 
