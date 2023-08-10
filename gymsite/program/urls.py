from django.urls import path
from . import views


urlpatterns = [
    path('', views.program_list, name='program_list'),  # jei tik /program atidaro program listą
    path('program_days/<int:program_id>/', views.program_days, name='program-days'),  # Atvaizduoti programos dienų sąrašą
    path('client_list/', views.client_list, name='client_list'),
    path('client_detail/<int:user_id>/', views.client_detail, name='client_detail'),
    # name naudojamas HTML'e
    path('generate_program_day_pdf/<int:programday_id>/', views.generate_program_day_pdf, name='generate_program_day_pdf'),
    # Sugeneruoti PDF
]