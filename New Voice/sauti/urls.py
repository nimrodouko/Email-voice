from django.urls import path
from . import views

urlpatterns = [
    path('send/',views.display_result, name= 'display'),
    path('',views.index, name= 'voice'),
    path('send-email/', views.send_email, name='mail'),
]
