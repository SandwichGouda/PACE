from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import list_pdfs

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.admin, name='admin'),
    path('pace/2023', list_pdfs, name='list_pdfs'),
    # path('pdfs/<path:filename>', views.serve_pdf, name='serve_pdf'),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
