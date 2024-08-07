from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('agregar-horario/', views.add_horario, name='agregar_horario'),
    path('agregar-profesional/', views.add_profesional, name='agregar_profesional'),
    path('listar-reservas/', views.listar_reservas, name='listar_reservas'),
]
