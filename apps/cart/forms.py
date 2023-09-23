from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    address = forms.CharField(max_length=250)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    stripe_token = forms.CharField(max_length=255)
