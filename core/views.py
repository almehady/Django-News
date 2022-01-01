from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
# Create your views here.


def index(request):
    latest_news = News.objects.all().filter(status='P', is_home=True).order_by('-id')[0:5]
    slider_news = News.objects.all().filter(status='P', is_home=True, top_news='S').order_by('-id')[0:4]
    six_news = News.objects.all().filter(status='P', is_home=True, top_news='6').order_by('-id')[0:6]
    world_news = News.objects.all().filter(status='P', is_home=True, main_category=1).order_by('-id')[0:4]
    popular_news = News.objects.all().filter(status='P', is_home=True, main_category=2).order_by('-id')[0:9]
    editor_choice = News.objects.all().filter(status='P', is_home=True, main_category=2).order_by('-id')[0:5]
    editor_choice_1 = editor_choice[0:1]
    editor_choice_4 = editor_choice[1:5]
    context = {
        'latest_news': latest_news,
        'slider_news': slider_news,
        'six_news': six_news,
        'world_news': world_news,
        'popular_news': popular_news,
        'editor_choice_1': editor_choice_1,
        'editor_choice_4' : editor_choice_4
    }
    return render(request, 'index.html', context)


class MainCategoryDetailView(DetailView):
    model = MainCategory
    paginate_by = 1
    template_name = 'main_category_detail.html'


def category(request, slug):
    latest_news = News.objects.all().filter(status='P', is_home=True).order_by('-id')[0:6]
    cat = get_object_or_404(MainCategory, slug=slug)
    contents = News.objects.filter(main_category=cat).order_by('-id')
    paginator = Paginator(contents, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'cat': cat,
        'page_obj': page_obj,
        'contents': contents,
        'latest_news': latest_news
    }
    return render(request, 'main_category_detail.html', context)


def news_details(request, slug):
    news_detail = News.objects.all().filter(slug=slug)
    current_news = get_object_or_404(News, slug=slug)
    you_may_like = News.objects.all().filter(main_category=current_news.main_category).order_by('-id').exclude(slug=slug)[0:5]
    context ={
        'news_detail': news_detail,
        'current_news': current_news,
        'you_may_like': you_may_like
    }
    return render(request, 'news_detail.html', context)

# class NewsDetailView(DetailView):
#     model = News
#     template_name = '.html'
