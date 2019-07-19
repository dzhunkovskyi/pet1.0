from django.http import HttpResponse
from django.db.models import F

from django.shortcuts import render

from .forms import ProductForm

from .models import Product


# Create your views here.
def create(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form': form
	}
	return render(request, "products/create.html", context)

# View to get all products
def get_all_products(request):
	products = Product.objects.filter(price__lt=8)
	context = {}
	print(products)
	for prod in products:
		print(prod.price)
		print(prod.price_new)

	# prod = products[0]
	# print(prod.price)
	# print(prod.price_new)
	# prod.save()

	return render(request, "home.html", context)
