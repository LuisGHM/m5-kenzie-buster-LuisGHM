from django.db import models
from movies.models import Movie
from users.models import User

# Create your models here.

class MovieOrder(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
