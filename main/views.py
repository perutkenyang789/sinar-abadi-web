from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    store_products = Product.objects.all()

    context = {
        'company' : 'Toko Sinar Abadi',
        'owner_name': 'Ida Made Revindra Dikta Mahendra',
        'owner_class': 'kelas PBP C',
        'store_proucts': store_products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)