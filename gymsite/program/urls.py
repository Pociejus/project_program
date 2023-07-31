from django.urls import path
from . import views

urlpatterns = [
    path('', views.program_list, name='program_list'),  # views.index yra funkcija views faile. name = index yra adreso pavadinimas
    path('program_days/<int:program_id>/', views.program_days, name='program-days'),  # Atvaizduoti programos dienų sąrašą
    path('generate_program_day_pdf/<int:programday_id>/', views.generate_program_day_pdf, name='generate_program_day_pdf'),  # Generuoti PDF programos dienai
]