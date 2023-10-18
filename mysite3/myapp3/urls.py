
from django.urls import path
from . import views
urlpatterns = [
 path('', views.home, name='home'),
 path('createcontact/', views.create_contact, name='create_contact'),
 path('contacts/', views.contact_list, name='contact_list'),
 path('contacts/update/<int:pk>/', views.update_contact, name='update_contact'),
 path('contacts/delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]