from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
		]

	email = forms.EmailField()
	# title = forms.CharField()

	def clean_email(self):
		email = self.cleaned_data['email']
		if not 'edu' in email:
			raise forms.ValidationError('No "edu" in email')
		return email

	def clean_title(self):
		title = self.cleaned_data['title']
		if not 'edu' in title:
			raise forms.ValidationError('No "edu" in title')
		return title