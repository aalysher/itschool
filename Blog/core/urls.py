from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('claim', views.Claim, name='claim'),
    path('course', views.course_info, name='course'),
    path('mentors', views.mentors_info, name='mentors'),
    path('details/<id>/', views.details, name='details')
] + static(settings.STATIC_URL, document_ROOT=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_ROOT=settings.MEDIA_ROOT)
