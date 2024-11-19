from . import views
from django.urls import path
urlpatterns = [
    path('', views.home_page),
    path('categories/', views.categories),
    path('cart/', views.user_carts)
]
