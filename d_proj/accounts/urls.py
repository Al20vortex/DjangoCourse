from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), #in this case, home refers to the home function defined above
    path('products/', views.products),
    path('customer/', views.customer),
]
