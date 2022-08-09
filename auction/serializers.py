from rest_framework import serializers

from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['average_price'] = instance.average_price
        rep['max_price'] = instance.max_price
        return rep


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'