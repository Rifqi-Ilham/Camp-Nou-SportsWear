import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    category = strip_tags(request.POST.get("category"))
    description = strip_tags(request.POST.get("description"))
    stock = request.POST.get("stock")
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user if request.user.is_authenticated else None

    new_product = Product(
        name=name,
        price=price,
        category=category,
        description=description,
        stock=stock or 0,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    # Return JSON response for AJAX success
    return JsonResponse({
        "status": "success",
        "message": "Product created successfully!",
        "product": {
            "id": str(new_product.id),
            "name": new_product.name,
            "price": new_product.price,
            "category": new_product.category,
            "description": new_product.description,
            "stock": new_product.stock,
            "thumbnail": new_product.thumbnail,
            "is_featured": new_product.is_featured,
            "user": new_product.user.username if new_product.user else "Anonymous"
        }
    }, status=201)

@csrf_exempt
def delete_product_ajax(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.delete()
        return JsonResponse({"status": "deleted"})
    except Product.DoesNotExist:
        return JsonResponse({"error": "not found"}, status=404)

@csrf_exempt
def update_product_ajax(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.name = strip_tags(request.POST.get("name"))
        product.price = request.POST.get("price")
        product.category = request.POST.get("category")
        product.stock = request.POST.get("stock")
        product.image_url = request.POST.get("image_url")
        product.description = strip_tags(request.POST.get("description"))
        product.is_featured = request.POST.get("is_featured") == "on"
        product.save()
        return JsonResponse({"status": "updated"})
    except Product.DoesNotExist:
        return JsonResponse({"error": "not found"}, status=404)


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    context = {
        "nama_aplikasi": "Camp Nou SportsWear",
        "nama": request.user.username,
        "npm": "2406495483",
        "kelas": "PBP-E",
        "product_list": product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    news = get_object_or_404(Product, pk=id)
    news.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }
    return render(request, "product_detail.html", {"product": product})

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'stock': product.stock,
            'thumbnail': product.thumbnail,
            'user_id': product.user.id if product.user else None,
            'username': product.user.username if product.user else "Anonymous",
        }
        for product in product_list
        ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'stock': getattr(product, 'stock', None),
            'thumbnail': product.thumbnail if getattr(product, 'thumbnail', None) else None,
            'is_featured': getattr(product, 'is_featured', False),
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Product not found'}, status=404)
   
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
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

