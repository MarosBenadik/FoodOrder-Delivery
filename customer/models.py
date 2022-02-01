from django.db import models

class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='menu_images/')
	price = models.DecimalField(max_digits=7, decimal_places=2)
	category = models.ManyToManyField('Category', related_name='item')
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name



class OrderModel(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	items = models.ManyToManyField('ItemQuantity', related_name='order', blank=True)
	name = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	street = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=100, blank=True)
	state = models.CharField(max_length=100, blank=True)
	zipcode = models.IntegerField(null=True)
	is_paid = models.BooleanField(default=False)
	is_shippped = models.BooleanField(default=False)
	number = models.IntegerField(null=True)

	def __str__(self):
		return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'



class News(models.Model):
	topic = models.CharField(max_length=100, blank=True)
	image = models.ImageField(upload_to='menu_images/', default='news_images/default.jpg')
	body = models.TextField(max_length=100, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)


class ItemQuantity(models.Model):
	item = models.ForeignKey('MenuItem', on_delete=models.DO_NOTHING)
	item_quantity = models.IntegerField(null=True, default=1)