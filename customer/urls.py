from django.urls import path
from .views import Index, About, Order, OrderConfirmation, OrderPayConfirmation, NoPaymentConfirmation, Basket

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('about/', About.as_view(), name='about'),
	path('order/', Order.as_view(), name='order'),
	path('order-confirmation/<int:pk>/', OrderConfirmation.as_view(), name='order-confirmation'),
	path('payment-confirmation/<int:pk>/', OrderPayConfirmation.as_view(), name='payment-submitted'),
	path('non-payment-submited/<int:pk>/', NoPaymentConfirmation.as_view(), name='non-payment-submitted'),
	path('basket/<int:pk>/', Basket.as_view(), name='basket')
]