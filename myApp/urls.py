from django.urls import path
from myApp import views
urlpatterns = [
    
    path('list/',views.list,name='list'),
    path('create/',views.create,name='create'),
    path('register/', views.register,name='register'),
    path('detailsstd/<int:idn>/', views.details,name='details'),
    path('edit/<int:id>/', views.edit_student,name='edit'),
]