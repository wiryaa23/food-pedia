from django.shortcuts import render

def show_main(request):
    context = {
        'app': 'Food Pedia',
        'name': 'Wirya Dharma Kurnia',
        'class': 'PBP C',
        'items': [
            {'name': 'Ayam Sakalan', 'price': 17000, 'description': 'Saudara Ayam Kalasan, lebih murah seribu', 'stock': 10, 'rating': 5.0},
            {'name': 'Janapese Food', 'price': 14000, 'description': 'Saudari Japanese Food, lebih murah seribu', 'stock': 10, 'rating': 5.0},
        ]
    }

    return render(request, "main.html", context)
