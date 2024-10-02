from .models import Category

def categoryView(request):
    categories = Category.objects.all()

    return {'categories':categories}