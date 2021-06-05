from .models import MainCategory

def header_category(request):
    return {
        'menu_category': MainCategory.objects.all().filter(featured=True).order_by('sequence'),
    }