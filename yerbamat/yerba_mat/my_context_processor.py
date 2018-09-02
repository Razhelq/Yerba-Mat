from .models import Category

def cats_cp(request):
    cats = Category.objects.all()
    return {'cats': cats}