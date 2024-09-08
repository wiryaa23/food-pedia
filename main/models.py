from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5
    