from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('Add/', views.AddUser, name='user-add'),
    path('Edit/<int:id>/', views.EditUser, name='user-edit'),
    path('Delete/<int:eid>/', views.DeleteUser, name='user-delete'),
    path('View/<int:eid>/', views.ViewUser, name='user-view'),
]
