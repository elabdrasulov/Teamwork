from django.shortcuts import get_object_or_404

from rest_framework import mixins
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import BetSerializer, CarSerializer

from .models import *

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class BetViewSet(
                mixins.DestroyModelMixin,
                GenericViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    @action(['POST'], detail=True)
    def create_bet(self, request, pk):
        user = request.user
        car = get_object_or_404(Car, id=pk)
        value = request.POST.get('price')
        
        if Bet.objects.filter(user=user, car=car).exists():
            bet = Bet.objects.get(user=user, car=car)
            bet.price = value
            bet.save()
        else:
            Bet.objects.create(user=user, car=car, price=value)

        return Response("Bet created")
    
    @action(['DELETE'], detail=True)
    def delete_bet(self, request, pk):
        user = request.user
        car = get_object_or_404(Car, id=pk)

        if Bet.objects.filter(user=user, car=car).exists():
            bet = Bet.objects.get(user=user, car=car)
            bet.price = 0
            bet.save()
        return Response("Bet deleted")

    

    

    
