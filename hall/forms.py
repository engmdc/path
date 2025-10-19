from django import forms
from .models import Hall, Facility, EventType

class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event type name'}),
        }

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'description', 'additional_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter facility name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter facility description'}),
            'additional_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}),
        }

class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = [
            'name', 'location', 'capacity', 'price_per_guest',
            'facilities', 'income_account', 'extra_income_account',
            'receivable_account', 'description', 'is_available'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter hall name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter hall location here'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'price_per_guest': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}),
            'facilities': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add facilities'}),
            'income_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Income Account Number'}),
            'extra_income_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Extra Income Account Number'}),
            'receivable_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Receivable Number'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter hall description'}),
            'is_available': forms.HiddenInput(),
        }
