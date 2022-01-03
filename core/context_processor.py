from .models import MainCategory, Page

def header_category(request):
    return {
        'menu_category': MainCategory.objects.all().filter(featured=True).order_by('sequence'),
        'footer_pages': Page.objects.all().filter(status='P').order_by('sequence')
    }
