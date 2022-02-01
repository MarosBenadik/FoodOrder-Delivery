from django.urls import path
from .views import MenuItemView, CategoryItemView, OrdersView, ItemQuantityView, OrderView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	path('menu-items/', MenuItemView.as_view()),
	path('category/', CategoryItemView.as_view()),
	path('orders/', OrdersView.as_view()),
	path('items-quantity/', ItemQuantityView.as_view()),
	path('orders/order/<int:pk>/', OrderView.as_view())

]