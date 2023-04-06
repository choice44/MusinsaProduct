from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/erp')
    else:
        return redirect('/sign-in')


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'erp/home.html', {'products': products})


@login_required
def product_create(request):
    # 상품 등록 view
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, 'erp/create.html', {'form': form})
