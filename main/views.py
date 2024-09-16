from django.shortcuts import render, redirect
from main.forms import FoodEntryForm
from main.models import FoodEntry
from django.http import HttpResponse
from django.core import serializers

# Add 'items'
def show_main(request):
    default_items = [
            {'name': 'Ayam Sakalan', 
             'price': 17000, 
             'description': 'Saudara Ayam Kalasan, lebih murah seribu', 
             'quantity': 10,
             'rating': 4.9,
            #  'image': 'https://cdn0-production-images-kly.akamaized.net/1YA9f59BW9DMtBK-QFTlUPjwZbw=/640x640/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/3515230/original/048321300_1626697063-E6lmxG9VgAIYOuG.jpg'
            },
            {'name': 'Janapese Food',
            'price': 14000,
            'description': 'Saudari Japanese Food, lebih murah seribu',
            'quantity': 10,
            'rating': 5.0,
            # 'image' : 'https://asset-a.grid.id/crop/0x0:960x691/x/photo/2019/01/24/2157661450.jpg'},
            }
        ]

    food_entries = FoodEntry.objects.all()

    database_items = []
    for entry in food_entries:
        database_items.append({'name': entry.name, 'price': entry.price, 'description': entry.description, 'quantity': entry.quantity, 'rating': entry.rating})
    
    all_entry = default_items + database_items
    context = {
        'app': 'Food Pedia',
        'name': 'Wirya Dharma Kurnia',
        'class': 'PBP C',
        'food_entries': all_entry,
    }
    return render(request, "main.html", context)


def create_food_entry(request):
    form = FoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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