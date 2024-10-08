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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
# Add 'items'
def show_main(request):

    # food_entries = FoodEntry.objects.filter(user=request.user)

    context = {
        'app': 'Food Pedia',
        'name': request.user.username,
        'class': 'PBP C',
        # 'food_entries': food_entries,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, "main.html", context)


def create_food_entry(request):
    form = FoodEntryForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user
            food_entry.save()
            return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_food_entry.html", context)

def show_xml(request):
    data = FoodEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = FoodEntry.objects.filter(user=request.user)
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
    # try:
    #     food = FoodEntry.objects.get(pk=id) 
    # except FoodEntry.DoesNotExist:
    #     return HttpResponse("Food not found", status=404)  

    # if request.method == 'POST':
    #     name = strip_tags(request.POST.get("name"))
    #     description = strip_tags(request.POST.get("description"))
    #     price = request.POST.get("price")
    #     quantity = request.POST.get("quantity")
    #     rating = request.POST.get("rating")
    #     # user = request.user

    #     food.name=name
    #     food.description=description
    #     food.price=price
    #     food.quantity=quantity
    #     food.rating=rating
    #     food.save()

    #     return redirect('main:show_main')

    # return render(request, 'edit_food.html', {'food': food})
# -----
    # food = FoodEntry.objects.get(pk=id)
    # form = FoodEntryForm(instance=food)

    # if request.method == "POST":
    #     if form.is_valid():
    #         name = strip_tags(request.POST.get("name"))
    #         description = strip_tags(request.POST.get("description"))
    #         price = request.POST.get("price")
    #         quantity = request.POST.get("quantity")
    #         rating = request.POST.get("rating")
            
    #         food.name=name
    #         food.description=description
    #         food.price=price
    #         food.quantity=quantity
    #         food.rating=rating
    #         food.save()
    #         return redirect('main:show_main')
    
    # context = {'food': food}
    # return render(request, "edit_food.html", context)
# ------
    food = FoodEntry.objects.get(pk=id)
    if request.method == "POST":
        form = FoodEntryForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = FoodEntryForm(instance=food)

    context = {'form': form, 'food': food}
    return render(request, "edit_food.html", context)


    # food = FoodEntry.objects.get(pk = id)
    # form = FoodEntryForm(request.POST or None, instance=food)

    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('main:show_main'))


    # context = {'form': form}
    # return render(request, "edit_food.html", context)


def delete_food(request, id):
    food = FoodEntry.objects.get(pk = id)
    food.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
# def add_food_entry_ajax(request):
#     form = FoodEntryForm(request.POST)

#     if form.is_valid():
#         # If the form is valid, save it
#         food_entry = form.save(commit=False)
#         food_entry.user = request.user  # Assign the user
#         food_entry.save()
#         return HttpResponse(b"CREATED", status=201)
    
#     # If the form is invalid, return errors
#     errors = form.errors.as_json()
#     return HttpResponse(errors, status=400, content_type="application/json")


def add_food_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = strip_tags(request.POST.get("price"))
    quantity = strip_tags(request.POST.get("quantity"))
    rating = strip_tags(request.POST.get("rating"))
    user = request.user

    new_food = FoodEntry(
        name=name,
        description=description,
        price=price,
        quantity=quantity,
        rating=rating,
        user=user

    )

    form = FoodEntryForm(request.POST, instance=new_food)
    if form.is_valid():
        new_food.save()
        return HttpResponse(b"CREATED", status=201)
    else:
        errors = form.errors.as_json()
        return HttpResponse(errors, status=400, content_type="application/json")
    