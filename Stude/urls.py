from django.urls import path
from . import views

urlpatterns = [
    path('view_own_record/', views.view_own_record, name='view_own_record'),
    path('edit_personal_details/', views.edit_personal_details, name='edit_personal_details'),
]

