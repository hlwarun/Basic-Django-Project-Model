from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('about/', views.about, name = 'aboutpage')
]
