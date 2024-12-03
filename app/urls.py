from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('customize_show/', views.customize_show, name='customize_show'),
    path('fashion_show/', views.fashion_show, name='fashion_show'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

