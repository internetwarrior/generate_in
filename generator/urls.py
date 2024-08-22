from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views

urlpatterns = [
path('invoice/',views.invoice),
path('receipt/update/<uuid:pk>',views.update_receipt),
path('config/', views.get_config),
    path('receipts/<uuid:pk>/', views.get_receipt, name='get_receipt'),
    path('receipts/<uuid:pk>/update/', views.update_receipt, name='update_receipt'),
]





