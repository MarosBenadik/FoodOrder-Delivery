from django.urls import path, include
from .views import Index, About, Order, OrderWithBasket, CustomerInformation, OrderConfirmation, ItemView, OrderPayConfirmation, NoPaymentConfirmation, Basket
from . import api

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('about/', About.as_view(), name='about'),
	path('order/', Order.as_view(), name='order'),
	path('updateorder/<int:pk>/', OrderWithBasket.as_view(), name='updateorder'),
	path('order/<int:pk>/customer-details/', CustomerInformation.as_view(), name='customer-details'),
	path('order-confirmation/<int:pk>/', OrderConfirmation.as_view(), name='order-confirmation'),
	path('payment-confirmation/<int:pk>/', OrderPayConfirmation.as_view(), name='payment-submitted'),
	path('non-payment-submited/<int:pk>/', NoPaymentConfirmation.as_view(), name='non-payment-submitted'),
	path('items/<int:pk>/basket/', Basket.as_view(), name='basket'),
	path('items/<int:pk>/', ItemView.as_view(), name='item-desctiption')
]