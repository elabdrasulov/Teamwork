from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Bet(models.Model):
    user = models.ForeignKey(User, related_name='bets', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.ForeignKey(Car, related_name='bets', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user} -> {self.price}"
    


