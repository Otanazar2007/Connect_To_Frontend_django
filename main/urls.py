from . import views
from django.urls import path
urlpatterns = [
    path('', views.home_page),
    path('categories/<int:pk>', views.categories_page, name='categories_page'),
    path('cart/', views.user_carts)
]