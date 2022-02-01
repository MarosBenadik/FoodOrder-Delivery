from django.shortcuts import render, redirect
from django.views import View
from django.utils.timezone import datetime
from customer.models import OrderModel, MenuItem
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class Dashboard(UserPassesTestMixin, LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		today = datetime.today()
		orders = OrderModel.objects.filter(
			created_on__year=today.year, created_on__month=today.month, created_on__day=today.day).order_by('-created_on')

		unshipped_orders = []

		total_revenue = 0
		for order in orders:
			total_revenue += order.price

			if not order.is_shippped:
				unshipped_orders.append(order)

		context = {
			'orders': unshipped_orders,
			'total_revenue': total_revenue,
			'total_orders': len(orders)
		}

		return render(request, 'restourant/dashboard.html', context)

	def test_func(self):
		return self.request.user.groups.filter(name='staff').exists()


class OrderDetails(UserPassesTestMixin, LoginRequiredMixin, View):
	def get(self, request, pk, *args, **kwargs):
		order = OrderModel.objects.get(pk=pk)
		items = order.items


		context = {
			'order': order,
			'items': items
		}

		return render(request, 'restourant/order-details.html', context)

	def post(self, request, pk, *args, **kwargs):

		order = OrderModel.objects.get(pk=pk)

		if request.POST.get('is_paid'):

			order.is_paid = True
			order.save()

		if request.POST.get('is_shipped'):

			order.is_shippped = True
			order.save()

		context = {
			'order': order
		}

		return render(request, 'restourant/order-details.html', context)

	def test_func(self):
		return self.request.user.groups.filter(name='staff').exists()

# Create your views here.

class AllOrders(UserPassesTestMixin, LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		orders = OrderModel.objects.all().order_by('-created_on')

		items_count = {}

		total_revenue = 0

		for order in orders:
			total_revenue += order.price

		context = {
			'orders': orders,
			'total_revenue': total_revenue,
			'total_orders': len(orders)
		}

		return render(request, 'restourant/all-orders.html', context)


	def test_func(self):
		return self.request.user.groups.filter(name='staff').exists()


class AddProduct(UserPassesTestMixin, LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		return render(request, 'restourant/add-item.html')

	def post(self, request, *args, **kwargs):

		name = request.POST.get('name')
		description = request.POST.get('description')
		image = request.POST.get('image')
		price = request.POST.get('price')
		category = request.POST.get('category')

		MenuItem.create(name=name, description=description, image=image, price=price, category=category)

		return redirect('dashboard')

	def test_func(self):
		return self.request.user.groups.filter(name='staff').exists()