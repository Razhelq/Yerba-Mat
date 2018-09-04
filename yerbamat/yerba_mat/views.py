from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from yerba_mat.models import Category, Product
from yerba_mat.forms import CategoryForm, ProductForm, ProductForm2, LoginForm


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')


class CategoryView(View):

    def get(self, request, id):
        category = Category.objects.get(id=id)
        products = Product.objects.all()
        return render(request, 'category_view.html', {'category': category, 'products': products})


class ProductAddView(View):

    def get(self, request):
        form = ProductForm2()
        return render(request, 'product_add.html', {'form': form})

    def post(self, request):
        form = ProductForm2(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('index')
        return render(request, 'product_add.html', {'error': 'Form is not valid'})


class CategoryAddView(View):

    def get(self, request):
        form = CategoryForm()
        return render(request, 'category_add.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('index')
        return render(request, 'category_add.html', {'error': 'Form is not valid'})


class ProductView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products_view.html', {'products': products})


class ProductDetailsView(View):

    def get(self, request, id):

        categories = Category.objects.all()
        product = Product.objects.get(id=id)
        return render(request, 'product_details.html', {'product': product, 'categories': categories})


class BasketView(View):
    pass


class LoginView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
        return redirect('index')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index')
        return redirect('index')


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('index')
        return redirect('login')

class ClientCreateView(View):

    def get(self, request):
        pass

