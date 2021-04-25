from django.urls import path
from . import views

app_name = 'graph'

urlpatterns = [
    path('get-equation-data/', views.LinearEquationAPI.as_view(), name='equation-data'),
    path('', views.LinearEquationView.as_view(), name="graph-home"),
]
