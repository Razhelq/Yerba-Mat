from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from yerba_mat.models import Category, Product, Client, Basket, InsideBasket, Order
from yerba_mat.forms import CategoryForm, ProductForm, ProductForm2, LoginForm, ClientCreateForm, BasketForm, OrderForm


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')


class CategoryView(View):

    def get(self, request, id):
        category = Category.objects.get(id=id)
        products = Product.objects.filter(category__id=id)
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
        form = BasketForm()
        product = Product.objects.get(id=id)
        return render(request, 'product_details.html', {'product': product, 'form': form})


class BasketView(View):

    def get(self, request):
        if request.user.is_authenticated:
            try:
                basket = Basket.objects.get(person=Client.objects.get(user__username=request.user))
                inside_baskets = InsideBasket.objects.filter(basket=basket)
                return render(request, 'basket_view.html', {'basket': basket, 'inside_baskets': inside_baskets})
            except ObjectDoesNotExist:
                return render(request, 'basket_view.html')
        return redirect('login')

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
        form = ClientCreateForm()
        return render(request, 'client_create.html', {'form': form})

    def post(self, request):
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            Client.objects.create(
                user=User.objects.get(username=form.cleaned_data['username']),
                name=form.cleaned_data['name'],
                lastname=form.cleaned_data['lastname'],
                street=form.cleaned_data['street'],
                post=form.cleaned_data['post'],
                city=form.cleaned_data['city'],
                phone=form.cleaned_data['phone']
            )
            return redirect('login')
        return redirect('client-create')


class AddProductToBasketView(View):

    def post(self, request, id):
        if request.user.is_authenticated:
            form = BasketForm(request.POST)
            if form.is_valid():
                try:
                    basket = Basket.objects.get(person=Client.objects.get(user__username=request.user))
                    try:
                        inside_basket = InsideBasket.objects.filter(basket=basket).get(product__id=id)
                        inside_basket.items = form.cleaned_data['items']
                        print(inside_basket.items)
                        inside_basket.save()
                    except ObjectDoesNotExist:
                        print(basket)
                        InsideBasket.objects.create(
                            basket=basket,
                            product=Product.objects.get(id=id),
                            items=form.cleaned_data['items']
                        )
                    inside_baskets = InsideBasket.objects.filter(basket=basket)
                    basket.total_price = 0
                    for inside in inside_baskets:
                        basket.total_price += inside.items * inside.product.price
                    basket.save()
                    return redirect('basket')
                except ObjectDoesNotExist:
                    Basket.objects.create(
                        person=Client.objects.get(user__username=request.user)
                    )
                    try:
                        inside_basket = InsideBasket.objects.get(product__id=id)
                        inside_basket.items = form.cleaned_data['items']
                        print(inside_basket.items)
                        inside_basket.save()
                    except ObjectDoesNotExist:
                        InsideBasket.objects.create(
                            basket=basket,
                            product=Product.objects.get(id=id),
                            items=form.cleaned_data['items']
                        )
                    basket = Basket.objects.get(person=Client.objects.get(user__username=request.user))
                    inside_baskets = InsideBasket.objects.filter(basket=basket)
                    basket.total_price = 0
                    for inside in inside_baskets:
                        print(inside.items)
                        basket.total_price += inside.items * inside.product.price
                    basket.save()
                    return redirect('basket')
            return redirect('product-details', id=id)
        return redirect('login')


class ModifyInsideBasketView(View):

    def post(self, request):
        basket = Basket.objects.get(person=Client.objects.get(user__username=request.user))
        inside_baskets = InsideBasket.objects.filter(basket=basket)
        for inside_basket in inside_baskets:
            if str(inside_basket.id) == request.POST.get('{}'.format(inside_basket.id)):
                inside_basket.items = request.POST.get(inside_basket.product.name)
                inside_basket.save()
        basket.total_price = 0
        for inside in InsideBasket.objects.filter(basket=basket):
            basket.total_price += inside.items * inside.product.price
        basket.save()
        return redirect('basket')


class OrderCreateView(View):

    def get(self, request):
        form = OrderForm(instance=get_object_or_404(Client, user=request.user))
        return render(request, 'order_form.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST, instance=get_object_or_404(Client, user=request.user))
        if form.is_valid():
            person = Client.objects.get(user__username=request.user)
            basket = Basket.objects.get(person=person)
            try:
                order = Order.objects.get(person=person)
                order.basket = basket
                order.person = person
                order.name = form.cleaned_data['name']
                order.lastname = form.cleaned_data['lastname']
                order.street = form.cleaned_data['street']
                order.post = form.cleaned_data['post']
                order.city = form.cleaned_data['city']
                order.phone = form.cleaned_data['phone']
                order.save()
            except ObjectDoesNotExist:
                Order.objects.create(
                    basket=basket,
                    person=person,
                    name=form.cleaned_data['name'],
                    lastname=form.cleaned_data['lastname'],
                    street=form.cleaned_data['street'],
                    post=form.cleaned_data['post'],
                    city=form.cleaned_data['city'],
                    phone=form.cleaned_data['phone']
                )
            return redirect('order-to-send')
        return redirect('basket')
