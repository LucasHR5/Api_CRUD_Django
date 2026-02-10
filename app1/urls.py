from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'clients',viewsets.ClientViewSet)
router.register(r'employees', viewsets.EmployeeViewSet)
router.register(r'products', viewsets.ProductViewSet)
router.register(r'sales', viewsets.SaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

