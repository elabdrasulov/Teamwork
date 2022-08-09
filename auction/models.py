from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):

    body_case = (
                ('sedan', "Седан"), 
                ('universal', "Универсал"), 
                ('kupe', "Купе"),
                ('hetchbek', "Хэтчбек"),
                ('miniven', "Минивен"),
                ('jeep', "Внедорожник"),
                ('pikap', "Пикап")
    )
    mark = models.CharField(max_length=50)
    model_car = models.CharField(max_length=50)
    year = models.IntegerField(blank=True, null=True)
    body_type = models.CharField(choices=body_case, max_length=100, blank=True)
    
    @property
    def average_price(self):
        prices = [p.price for p in self.bets.all()]
        if prices:
            for price in prices:
                if price == 0:
                    prices.remove(price)
            return round(sum(prices) / len(prices), 2)
        return 0

    @property
    def max_price(self):
        # prices = [p.price for p in self.bets.all()]
        prices = {str(u.user): p.price for u, p in zip(self.bets.all(), self.bets.all())}
        if prices:
            max_val = max(prices.values())
            res = {k:v for k, v in prices.items() if v == max_val}
            return res
        return 0

    def __str__(self):
        return self.mark

class Bet(models.Model):
    user = models.ForeignKey(User, related_name='bets', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.ForeignKey(Car, related_name='bets', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user} -> {self.price}"
