from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView
from .views import category


urlpatterns = [
        path('', TemplateView.as_view(template_name="index.html")),
        path('<slug:slug>/', category, name='main-category-detail'),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
