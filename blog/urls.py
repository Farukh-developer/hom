from django.urls import path
from .views import LoginView, RegisterView
from .views import data, read_data, delete_data

urlpatterns = [
   
   path('',LoginView.as_view(), name='login'),
   path('register/', RegisterView.as_view(), name='register'),
   path('data', data, name='data'),
   path('read_data/<int:id>/',read_data, name='read_data'),
   path('delete_data/<int:id>/',delete_data, name='delete_data'),
   
   

    
]
