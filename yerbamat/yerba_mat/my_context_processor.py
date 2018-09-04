from .models import Category

def cats_cp(request):
    cats = Category.objects.all()
    user = request.user
    return {'cats': cats, 'user': user}