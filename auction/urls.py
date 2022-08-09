from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, BetViewSet


router = DefaultRouter()
router.register("cars", CarViewSet, basename='cars')
router.register("bets", BetViewSet, basename='bets')


urlpatterns = [
    path('', include(router.urls)),
    # path('bet/<int:c_id>/', create_bet),
]