from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone
from .models import Product, Inventory
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


@login_required
def inventory(request, product_id):
    """
    inbound_create, outbound_create view에서 만들어진 데이터를 합산합니다.
    Django ORM을 통하여 총 수량, 가격등을 계산할 수 있습니다.
    """
    product = get_object_or_404(Product, pk=product_id)
    inven = Inventory.objects.filter(product=product).first()
    if not inven:
        inven = Inventory(product=product)
    total_inbounds_quantity = 0
    total_inbounds_price = 0
    total_outbounds_quantity = 0
    total_outbounds_price = 0
    # 총 입고 수량, 가격 계산
    inbounds = product.inbound_set.all()
    for inbound in inbounds:
        total_inbounds_quantity += inbound.quantity
        total_inbounds_price += inbound.amount

    # 총 출고 수량, 가격 계산
    outbounds = product.outbound_set.all()
    for outbound in outbounds:
        total_outbounds_quantity += outbound.quantity
        total_outbounds_price += outbound.amount
    inven.stock_quantity = total_inbounds_quantity - total_outbounds_quantity
    inven.save()

    context = {'inventory': inven,
               'product': product,
               'inbounds': inbounds,
               'outbounds': outbounds,
               'total_inbounds_quantity': total_inbounds_quantity,
               'total_outbounds_quantity': total_outbounds_quantity,
               'total_inbounds_price': total_inbounds_price,
               'total_outbounds_price': total_outbounds_price,
               }

    return render(request, 'erp/inventory.html', context)
