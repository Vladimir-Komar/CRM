from django.shortcuts import render, redirect
from .models import Customer, Provider, Product, Deal
from .forms import CustomerForm, ProviderForm, ProductForm, DealForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url="user:login")
def customer(request):
    form = CustomerForm(request.POST or None, request.FILES or None)

    if request.method == "GET":
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

    if request.method == "POST":
        customers = form.save(commit=False)
        customers.save()
        messages.success(request, "Клиент успешно добавлен!!!")
        return redirect("crm:customer")


@login_required(login_url="user:login")
def provider(request):
    form = ProviderForm(request.POST or None, request.FILES or None)
    if request.method == "GET":
        providers = Provider.objects.all()
        return render(request, "provider.html", {"provider": providers, "form": form})

    if request.method == "POST":
        if form.is_valid():
            providers = form.save(commit=False)
            providers.save()
            messages.success(request, "Поставщик успешно добавлен!!!")
        return redirect("crm:provider")


@login_required(login_url="user:login")
def product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == "GET":
        products = Product.objects.all()
        return render(request, "product.html", {"product": products, "form": form})

    if request.method == "POST":
        if form.is_valid():
            products = form.save(commit=False)
            products.save()
            messages.success(request, "Лекарство успешно добавлено!!!")
        return redirect("crm:product")


@login_required(login_url="user:login")
def deal(request):
    form = DealForm(request.POST or None, request.FILES or None)
    if request.method == "GET":
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

    if request.method == "POST":
        if form.is_valid():
            # print(form.cleaned_data)
            # print('\n'.join(dir(form.cleaned_data)))
            deal_date = form.cleaned_data['deal_date']
            customers = form.cleaned_data['customer']
            products = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            deal_price = form.cleaned_data['deal_price']
            full = form.cleaned_data['product']
            price = full.price
            total = (deal_price - price) * quantity
            b = Deal(deal_date=deal_date, customer=customers, product=products, quantity=quantity,
                     deal_price=deal_price, profit=total)
            b.save()

            messages.success(request, "Сделка сохранена!!!")
            return redirect("crm:deal")


