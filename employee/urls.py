from django.urls import path
from . import views
urlpatterns = [
    path('', views.details, name= 'details'),
    path('opentravelrequestform/', views.travelform, name= 'travelform'),
    path('openreimbursementform/', views.reimbursementform, name= 'reimbursementform'),


    ]