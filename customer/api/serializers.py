from rest_framework import serializers
from customer.models import MenuItem, Category, OrderModel, ItemQuantity


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
	category = CategorySerializer(many=True)
	class Meta:
		model = MenuItem
		fields = '__all__'

class MenuItemSerializerNoCategory(serializers.ModelSerializer):

	class Meta:
		model = MenuItem
		fields = '__all__'


class ItemQuantitySerializer(serializers.ModelSerializer):

	class Meta:
		model = ItemQuantity
		fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
	items = ItemQuantitySerializer(many=True)
	class Meta:
		model = OrderModel
		fields = '__all__'





