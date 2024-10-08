from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
   # path('about/', views.about, name='about'),
    path('about/', views.about, name='about-page'),
    # path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills-page'),
    # path('about/', views.about, name='about'),
]
