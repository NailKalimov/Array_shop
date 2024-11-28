from django.urls import path
from . import views


app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('complited/', views.payment_completed, name='complited'),
    path('canceled/', views.payment_canceled, name='canceled'),
]