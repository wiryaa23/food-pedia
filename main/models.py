import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class FoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)])
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )


    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5
    