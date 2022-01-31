from django.contrib import admin
from django.urls import path, include
from .views import Dashboard, OrderDetails, AllOrders, AddProduct


urlpatterns = [
	path('dashboard', Dashboard.as_view(), name='dashboard'),
	path('orders/<int:pk>/', OrderDetails.as_view(), name='order-details'),
	path('allorders', AllOrders.as_view(), name='all-orders'),
	path('add-product/', AddProduct.as_view(), name='add-item')

]