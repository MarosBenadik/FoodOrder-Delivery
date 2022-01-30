from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail

from .models import MenuItem, Category, OrderModel


class Index(View):
	def get(self, request, *args, **kwargs):
		new_items = MenuItem.objects.all().order_by('-pk')[4:]

		most_ordered = OrderModel.objects.filter()

		context = {
			'new_items': new_items
		}


		return render(request, 'customer/index.html', context)


class About(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'customer/about.html')


class Order(View):
	def get(self, request, *args, **kwargs):
		appetizers = MenuItem.objects.filter(category__name__contains="predjedlo")
		entres = MenuItem.objects.filter(category__name__contains="hlavnejedlo")
		soups = MenuItem.objects.filter(category__name__contains="polievka")
		desserts = MenuItem.objects.filter(category__name__contains="dezerty")
		drinks = MenuItem.objects.filter(category__name__contains="napoje")


		context = {
			'appetizers': appetizers,
			'entres': entres,
			'soups': soups,
			'desserts': desserts,
			'drinks': drinks,
		}

		return render(request, 'customer/order.html', context)

	def post(self, request, *args, **kwargs):
		name = request.POST.get('name')
		email = request.POST.get('email')
		street = request.POST.get('street')
		city = request.POST.get('city')
		state = request.POST.get('state')
		zipcode = request.POST.get('zipcode')

		order_items = {
			'items': []
		}

		items = request.POST.getlist('items[]')

		for item in items:
			menu_item = MenuItem.objects.get(pk__contains=int(item))
			quantity = request.POST.get('quantity')

			item_data = {
				'id': menu_item.pk,
				'name': menu_item.name,
				'price': menu_item.price,
				'quantity': quantity
			}

			order_items['items'].append(item_data)


		price = 0
		item_ids = []


		for item in order_items['items']:
			item_price = item['price']
			price += item_price

			item_ids.append(item['id'])



		order = OrderModel.objects.create(
			price=price,
			name=name,
			email=email,
			street=street,
			city=city,
			state=state,
			zipcode=zipcode
		)
		order.items.add(*item_ids)

		context = {
			'items': order_items['items'],
			'price': price
		}

		return redirect('order-confirmation', pk=order.pk)


class OrderConfirmation(View):
	def get(self, request, pk, *args, **kwargs):
		order = OrderModel.objects.get(pk=pk)
		items = order.items
		context = {
			'pk': order.pk,
			'items': order.items,
			'price': order.price,

		}

		return render(request, 'customer/order_confirmation.html', context)

	def post(self, request, pk, *args, **kwargs):
		print(request.body)



class NoPaymentConfirmation(View):
	def get(self, request, pk, *args, **kwargs):
		order = OrderModel.objects.get(pk=pk)
		price = order.price
		email = order.email

		body = ('Dakujeme! Vasa objednavka sa zacala pripravovat a bude dorucena zachvilu!\n'
		        f'Cena objednavky: {price}\n'
		        'Vazime si vasu vernost'
		        )

		send_mail(
			'Dakujeme za vasu objednavku!',
			body,
			'example@example.com',
			[email],
			fail_silently=False
		)

		context = {
			'pk': order.pk,
			'items': order.items,
			'price': order.price
		}

		return render(request, 'customer/not_pay_order.html', context)



class OrderPayConfirmation(View):
	def get(self, request, pk, *args, **kwargs):
		order = OrderModel.objects.get(pk=pk)
		order.is_paid = True
		order.save()
		price = order.price
		email = order.email

		body = ('Dakujeme! Vasa objednavka sa zacala pripravovat a bude dorucena zachvilu!\n'
		        f'Cena objednavky: {price}\n'
		        'Vazime si vasu vernost'
		        )

		send_mail(
			'Dakujeme za vasu objednavku!',
			body,
			'example@example.com',
			[email],
			fail_silently=False
		)

		return render(request, 'customer/order_pay_confirmation.html')


class Basket(View):
	def get(self, request, pk, *args, **kwargs):
		order = OrderModel.objects.get(pk=pk)

		context = {
			'pk': order.pk,
			'items': order.items,
			'quantity': order.items.count(),
			'price': order.price
		}

		return render(request, 'customer/basket.html', context)



