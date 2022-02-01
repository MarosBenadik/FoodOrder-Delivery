from rest_framework import generics
from customer.models import MenuItem, Category, OrderModel, ItemQuantity
from .serializers import MenuItemSerializer, CategorySerializer, OrderSerializer, ItemQuantitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MenuItemView(APIView):
	def get(self, request):
		items = MenuItem.objects.all()
		serializer = MenuItemSerializer(items, many=True)
		return Response(serializer.data)


class CategoryItemView(APIView):
	def get(self, request):
		category = Category.objects.all()
		serializer = CategorySerializer(category, many=True)
		return Response(serializer.data)


class OrdersView(APIView):
	def get(self, request):
		orders = OrderModel.objects.all()
		serializer = OrderSerializer(orders, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = OrderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemQuantityView(APIView):
	def get(self, request):
		items = ItemQuantity.objects.all()
		serializer = ItemQuantitySerializer(items, many=True)
		return Response(serializer.data)


class OrderView(APIView):
	def get(self, request, pk):
		item = OrderModel.objects.get(pk=pk)
		serializer = OrderSerializer(item)
		return Response(serializer.data)
