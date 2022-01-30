from django.shortcuts import render
from django.views import View
from django.utils.timezone import datetime
from customer.models import OrderModel
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

		context = {
			'order': order
		}

		return render(request, 'restourant/order-details.html', context)

	def post(self, request, pk, *args, **kwargs):
		order = OrderModel.objects.get(pk=pk)

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

