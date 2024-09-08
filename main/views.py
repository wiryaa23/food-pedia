from django.shortcuts import render

def show_main(request):
    context = {
        'app': 'Food Pedia',
        'name': 'Wirya Dharma Kurnia',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
