from django.shortcuts import render, redirect
from .models import Customer, Provider, Product, Deal
from .forms import CustomerForm, ProviderForm, ProductForm, DealForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url="user:login")
def customer(request):
    form = CustomerForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        customers = form.save(commit=False)
        customers.save()
        messages.success(request, "Клиент успешно добавлен!!!")
        return redirect("crm:customer")

    customers = Customer.objects.all()
    paginator = Paginator(customers, 15)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        customersu = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        customersu = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        customersu = paginator.page(paginator.num_pages)

    return render(request, "customer.html", {"customer": customersu, "form": form})


@login_required(login_url="user:login")
def provider(request):
    form = ProviderForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        providers = form.save(commit=False)
        providers.save()
        messages.success(request, "Поставщик успешно добавлен!!!")
        return redirect("crm:provider")

    providers = Provider.objects.all()
    return render(request, "provider.html", {"provider": providers, "form": form})


@login_required(login_url="user:login")
def product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        products = form.save(commit=False)
        products.save()
        messages.success(request, "Лекарство успешно добавлено!!!")
        return redirect("crm:product")

    products = Product.objects.all()
    return render(request, "product.html", {"product": products, "form": form})


@login_required(login_url="user:login")
def deal(request):
    form = DealForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        deal_date = form.cleaned_data['deal_date']
        customer = form.cleaned_data['customer']
        product = form.cleaned_data['product']
        deal_price = form.cleaned_data['deal_price']
        full = form.cleaned_data['product']
        price = full.price
        total = deal_price - price
        b = Deal(deal_date=deal_date, customer=customer, product=product, deal_price=deal_price, profit=total)
        b.save()

        messages.success(request, "Сделка сохранена!!!")
        return redirect("crm:deal")

    deals = Deal.objects.all()

    paginator = Paginator(deals, 15)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        dealsu = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dealsu = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        dealsu = paginator.page(paginator.num_pages)

    return render(request, "deal.html", {"deal": dealsu, "form": form})
