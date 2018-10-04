from django.core.exceptions import ObjectDoesNotExist

from .models import Category, Basket, Client

def cats_cp(request):
    cats = Category.objects.all()
    user = request.user
    try:
        basket = Basket.objects.get(person=Client.objects.get(user__username=request.user)).total_price
    except ObjectDoesNotExist:
        basket = 0
    return {'cats': cats, 'user': user, 'bas': basket}