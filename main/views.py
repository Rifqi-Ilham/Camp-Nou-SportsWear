from main.models import Product
from django.shortcuts import render

def show_main(request):
    context = {
        "nama_aplikasi": "Camp Nou SportsWear",
        "nama": "Muhammad Rifqi Ilham",
        "npm": "2406495483",
    }
    return render(request, "main.html", context)
