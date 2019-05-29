from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
	print(request.user)
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs): # *args, **kwargs
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs): # *args, **kwargs
	dict_contest = {
		"my_text": 'This is text',
		"my_number": 1234,
		"my_list": [123, 123134, 124]
	}
	return render(request, "about.html", dict_contest)


def social_view(request, *args, **kwargs): # *args, **kwargs
	return render(request, "social.html", {})
