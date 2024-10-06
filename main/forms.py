from django.forms import ModelForm
from main.models import FoodEntry
from django.utils.html import strip_tags

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