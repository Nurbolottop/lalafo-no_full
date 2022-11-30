from django.shortcuts import render, redirect
from apps.settings.models import Setting
from apps.products.models import Product,ProductLike

# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    random_products = Product.objects.all().order_by('?')
    if request.method =="POST":
        try:
            like = ProductLike.objects.get(user = request.user, product = product)
            like.delete()
        except:
            ProductLike.objects.create(user = request.user, product = product)
    context = {
        'product' : product,
        'setting' : setting,
    }
    return render(request, 'single-product.html', context)

def product_create(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        product = Product.objects.create(user = request.user, title = title, description = description, image = image, price = price)
        return redirect('product_detail', product.id)
    context = {
        'setting' : setting,
    }
    return render(request, 'product_create.html', context)