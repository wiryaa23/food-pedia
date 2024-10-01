from django.shortcuts import render, redirect, reverse
from main.forms import FoodEntryForm
from main.models import FoodEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
# Add 'items'
def show_main(request):
    
    default_items = [
            {'name': 'Ayam Sakalan (Default)', 
             'price': 17000, 
             'description': 'Saudara Ayam Kalasan, lebih murah seribu', 
             'quantity': 10,
             'rating': 4.9,
            #  'image': 'https://cdn0-production-images-kly.akamaized.net/1YA9f59BW9DMtBK-QFTlUPjwZbw=/640x640/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/3515230/original/048321300_1626697063-E6lmxG9VgAIYOuG.jpg'
            },
            {'name': 'Janapese Food (Default)',
            'price': 14000,
            'description': 'Saudari Japanese Food, lebih murah seribu',
            'quantity': 10,
            'rating': 5.0,
            # 'image' : 'https://asset-a.grid.id/crop/0x0:960x691/x/photo/2019/01/24/2157661450.jpg'},
            }
        ]

    food_entries = FoodEntry.objects.filter(user=request.user)

    database_items = []
    for entry in food_entries:
        database_items.append({'name': entry.name, 'price': entry.price, 'description': entry.description, 'quantity': entry.quantity, 'rating': entry.rating, 'id': entry.id})
    
    all_entry = database_items
    context = {
        'app': 'Food Pedia',
        'name': request.user.username,
        'class': 'PBP C',
        'food_entries': all_entry,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, "main.html", context)


def create_food_entry(request):
    form = FoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        food_entry = form.save(commit=False)
        food_entry.user = request.user
        food_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_food_entry.html", context)

def show_xml(request):
    data = FoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = FoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = FoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = FoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete_item(request, pk):
    item = FoodEntry.objects.get(pk=pk)
    item.delete()
    return redirect('/')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Oops, incorrect username or password!")
            return redirect('main:login')
   else:
        form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_food(request, id):
    food = FoodEntry.objects.get(pk = id)
    form = FoodEntryForm(request.POST or None, instance=food)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_food.html", context)



def delete_food(request, id):
    food = FoodEntry.objects.get(pk = id)
    food.delete()
    return HttpResponseRedirect(reverse('main:show_main'))