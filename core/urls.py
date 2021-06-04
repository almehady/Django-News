from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView


urlpatterns = [
        path('', TemplateView.as_view(template_name="index.html")),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
