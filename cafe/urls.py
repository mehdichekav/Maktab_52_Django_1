from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contant/', views.contant, name='contant'),
    path('menu/', views.menu, name='menu'),
    path('receptis-print/', views.recepties, name='recepits-print')
    # path('<int:id>/<slug:slug>/', views.articles_detail, name='article_detail'),
]