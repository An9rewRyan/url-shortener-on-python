from django.urls import path
from main.models import Link
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shorten/', views.shorten, name='shorten'),
    path('<str:hash>/', views.redirect_, name = 'redir')
]