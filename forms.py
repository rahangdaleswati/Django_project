from django import forms
from .models import Order

customer_choice = [('OFF', 'offline'), ('ON', 'online')]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'del_date': 'Delivery Date',
            'del_address': 'Delivery Address'
        }
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'product_price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'del_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'del_address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'address'
            }),
            'gift_option': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'payment_mode': forms.Select(choices=customer_choice, attrs={
                'class': 'form-select form-select w-50'
            })
        }
