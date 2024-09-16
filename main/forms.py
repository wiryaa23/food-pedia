from django.forms import ModelForm
from main.models import FoodEntry

class FoodEntryForm(ModelForm):
    class Meta:
        model = FoodEntry   
        fields = ["name", "price", "description", "quantity", "rating"]