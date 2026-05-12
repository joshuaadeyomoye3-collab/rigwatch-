from django.urls import path
from . import views

urlpatterns = [
    path('', views.well_list, name='well-list'),
    path('<int:well_id>/', views.well_detail, name='well-detail'),
    path('<int:well_id>/status/', views.well_status, name='well-status')
]