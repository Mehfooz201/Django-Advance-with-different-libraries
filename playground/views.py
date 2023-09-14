from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    name = 'Mehfooz Alee'
    roll =  47

    context = {
        'name' : name,
        'roll': roll
    }
    return render(request, 'home.html', context)
