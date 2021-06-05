from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('claim', views.Claim, name='claim'),
    path('course', views.course_info, name='course'),
    path('mentors', views.mentors_info, name='mentors')
]
