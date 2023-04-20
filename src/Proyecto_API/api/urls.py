from django.urls import path
from .views import *

urlpatterns=[
    path('productos/', ProductView.as_view(), name='product_list'),
    path('productos/<int:id>', ProductView.as_view(), name='product_process')
]