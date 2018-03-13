from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.details, name= 'details'),
    path('opentravelrequestform/', views.travelform, name= 'travelform'),
    path('openexpenseform/', views.expenseform, name= 'expenseform'),
    path('viewtravelform/', views.viewtravelform, name= 'viewtravelform'),
    path('viewexpenseform/', views.viewexpenseform, name= 'viewexpenseform'),
    path('viewexpenseform/media/receipt=<receipt>/', views.viewexpenseformfiles, name= 'viewexpenseformfiles' ),

    ]
