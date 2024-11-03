from django.urls import path
from . import views

urlpatterns = [
    path('progress/', views.progress_list, name='progress_list'),
    path('progress/create/', views.progress_create, name='progress_create'),
    path('progress/update/<int:pk>/', views.progress_update, name='progress_update'),
    path('progress/delete/<int:pk>/', views.progress_delete, name='progress_delete'),
    
    path('sleeptrack/', views.sleeptrack_list, name='sleeptrack_list'),
    path('sleeptrack/create/', views.sleeptrack_create, name='sleeptrack_create'),
    path('sleeptrack/update/<int:pk>/', views.sleeptrack_update, name='sleeptrack_update'),
    path('sleeptrack/delete/<int:pk>/', views.sleeptrack_delete, name='sleeptrack_delete'),
]
