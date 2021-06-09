from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.core.paginator import Paginator
from django.db.models import Q
from .models import MainCategory, Content
# Create your views here.

class MainCategoryDetailView(DetailView):
    model = MainCategory
    paginate_by = 1
    template_name = 'main_category_detail.html'


def category(request, slug):
    latest_news = Content.objects.all().filter(status='P', is_home=True).order_by('-id')[0:6]
    cat = get_object_or_404(MainCategory, slug=slug)
    contents = Content.objects.filter(main_category=cat).order_by('-id')
    paginator = Paginator(contents, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'cat': cat,
        'page_obj': page_obj,
        'latest_content': latest_news
    }
    return render(request, 'main_category_detail.html', context)
