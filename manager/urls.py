from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('reviewtravelform/', views.reviewtravelform, name= 'reviewtravelform'),
    path('reviewexpenseform/', views.reviewexpenseform, name= 'reviewexpenseform'),
    ]