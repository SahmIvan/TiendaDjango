from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, StoreForm, ProductForm
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Store, Product, ShoppingCart, CartItem, Category, User



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == 'vendor':
                return redirect('vendorHome')
            else:
                return redirect('storeHome')
    else:
        form = CustomUserCreationForm()
    return render(request, 'AppTienda/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'vendor':
                    return redirect('vendorHome')
                else:
                    return redirect('storeHome')
    else:
        form = AuthenticationForm()
    return render(request, 'AppTienda/login.html', {'form': form})
# General Access
def store_list(request):
    stores = Store.objects.all()
    products = [store.product_set.first() for store in stores]
    return render(request, 'AppTienda/store_list.html', {'stores': stores, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'AppTienda/product_detail.html', {'product': product})


# Vendor Access Required ONLY
@login_required
def manage_store(request):
    try:
        store = Store.objects.get(user=request.user)
        if request.method == 'POST':
            form = StoreForm(request.POST, request.FILES, instance=store)
            if form.is_valid():
                form.save()
                return redirect('vendorHome')
        else:
            form = StoreForm(instance=store)
    except Store.DoesNotExist:
        if request.method == 'POST':
            form = StoreForm(request.POST, request.FILES)
            if form.is_valid():
                new_store = form.save(commit=False)
                new_store.user = request.user
                new_store.save()
                return redirect('vendorHome')
        else:
            form = StoreForm()

    return render(request, 'AppTienda/manage_store.html', {'form': form})

 
@login_required
def vendor_products(request):
    try:
        store = Store.objects.get(user=request.user)
        products = Product.objects.filter(store=store)
    except Store.DoesNotExist:
        return redirect('manage_store')  # Redirige al usuario para que cree su tienda primero

    return render(request, 'AppTienda/vendor_products.html', {'products': products})

@login_required
def create_product(request):
    try:
        store = Store.objects.get(user=request.user)
    except Store.DoesNotExist:
        return redirect('manage_store')  # Redirige al usuario para que cree su tienda primero

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.save()
            return redirect('vendor_products')
    else:
        form = ProductForm()

    categories = Category.objects.all()

    return render(request, 'AppTienda/create_product.html', {'form': form, 'categories': categories})

@login_required
def vendor_profile(request):
    user = request.user
    try:
        store = Store.objects.get(user=user)
    except Store.DoesNotExist:
        store = None

    context = {
        'user': user,
        'store': store,
    }
    return render(request, 'AppTienda/vendor_profile.html', context)

# Only customer can access, login is required
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('product_detail', product_id=product_id)

@login_required
def buy_now(request, product_id):
    add_to_cart(request, product_id)
    return redirect('checkout')
    
    
def storeHome(request):
    return render(request, 'AppTienda/storeHome.html')

@login_required
def vendorHome(request):
    return render(request, 'AppTienda/vendorHome.html')

