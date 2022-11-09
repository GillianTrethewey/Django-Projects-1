import random

from django.shortcuts import render, redirect

from .models import Shiba

def homepage(request):
    # Get all the Shibas from the database, put them into the variable "shibas"
    shibas = Shiba.objects.all()

    # Get the count of the shibas and put it into the variable "shiba_count"
    shiba_count = shibas.count()

    # This constructs the "template context dictionary" -- the dictionary that
    # contains the "template variable" data that we can render into the
    # template
    context = {
        'shiba_count': shiba_count,
        'all_shibas': shibas,
    }

    # "homepage.html" tells Django to look for the template in
    # `templates/homepage.html'
    return render(request, 'homepage.html', context)


def adopt_dog(request):
    context = {}  # No need for context on this page

    # Get a number from the POST request
    number = request.POST['number']
    print('They entered:', number)

    # Get the Shiba referenced by this number
    shiba = Shiba.objects.get(id=number)

    # ...and delete it!
    shiba.delete()

    # Let's send them back to '/'
    return redirect('/')

def add_dog(request):
    context = {}  # No need for context on this page

    if 'name' in request.POST:
        age = int(request.POST['age'])
        name = request.POST['name']
        print('They entered:', name)

        # Add a new Shiba to our database
        # For now, we'll just make them all have the same image
        Shiba.objects.create(
            age=age,
            name=name,
            image_src='https://i.imgur.com/VEslUBl.png',
        )

        # Finally, we'll just redirect to '/'
        return redirect('/')


    # "add_dog.html" tells Django to look for the template in
    # `templates/add_dog.html'
    return render(request, 'add_dog.html', context)

