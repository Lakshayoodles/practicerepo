from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.create_list, name="Student form"),
    path('list/', views.get_list, name='Student list'),
    path('delete/<int:id>', views.delete_list, name="delete"),

]
