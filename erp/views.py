from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone
from .models import Product
from .forms import ProductForm, InboundForm, OutboundForm


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


@login_required
@transaction.atomic
def inbound_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = InboundForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.inbound_date = timezone.now()
            answer.product = product
            product.stock_quantity += answer.quantity
            product.save()
            answer.save()
            return redirect('erp:inbound_create', product_id=product.id)
    else:
        form = InboundForm()
        context = {'product': product, 'form': form}
    return render(request, 'erp/inbound.html', context)


@login_required
@transaction.atomic
def outbound_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = OutboundForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.outbound_date = timezone.now()
            answer.product = product
            product.stock_quantity -= answer.quantity
            product.save()
            answer.save()
            return redirect('erp:outbound_create', product_id=product.id)
    else:
        form = OutboundForm()
        context = {'product': product, 'form': form}
    return render(request, 'erp/outbound.html', context)
