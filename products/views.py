from django.http import HttpResponse

from django.shortcuts import render

from .forms import ProductForm


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