from .models import BillingAddress
from django import forms


class CreateBillingAddress(forms.ModelForm):
	class Meta:
		model = BillingAddress
		fields = ('address', 'apartment_address', 'country', 'payment_choice', 'zipcode' ,'save_info')