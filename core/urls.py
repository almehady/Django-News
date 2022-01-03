from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView
from .views import *

app_name = 'core'

urlpatterns = [
        path('', views.index, name='home'),
        path('search/', views.search, name='search'),
        path('<slug:slug>/', category, name='main-category-detail'),
        path('news/<slug>/', views.news_details, name='news-detail'),
        path('tag/<slug:slug>/', views.tagged, name='tag-detail'),
        path('page/<slug:slug>/', PageDetailView.as_view(), name='page-detail'),


        # path('news/<slug:slug>/', NewsDetailView.as_view(), name='news-detail'),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
