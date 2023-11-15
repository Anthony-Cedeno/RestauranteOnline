from django.urls import path

from . import views

urlpatterns = [

    path('', views.marketplace, name='marketplace'),

    path('<slug:vendor_slug>/', views.vendor_detail, name='vendor_detail'),

    # Agregar al carrito
    path('add_to_cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    # Restar al carrito
    path('decrease_cart/<int:food_id>/', views.decrease_cart, name='decrease_cart'),
    # Eliminar item del carrito
    path('delete_cart/<int:cart_id>/', views.delete_cart, name='delete_cart'),

]
