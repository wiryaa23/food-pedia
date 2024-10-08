from django.forms import ModelForm
from main.models import FoodEntry
from django.utils.html import strip_tags
from django import forms

class FoodEntryForm(ModelForm):
    class Meta:
        model = FoodEntry   
        fields = ["name", "price", "description", "quantity", "rating"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 1:
            raise forms.ValidationError("The minimum price is 1.")
        return price
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 1:
            raise forms.ValidationError("The minimum quantity is 1.")
        return quantity
    
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0:
            raise forms.ValidationError("Rating must be between 0-5.")
        if rating > 5:
            raise forms.ValidationError("Rating must be between 0-5.")
        return rating