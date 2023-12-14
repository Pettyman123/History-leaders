from django.urls import path
from .import views
urlpatterns = [
    path('',views.ind),
    path('data/', views.get_data, name= 'details.html'),
    
]
