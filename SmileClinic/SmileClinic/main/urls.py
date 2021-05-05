from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.Index.as_view()),
    path('about_company/', views.about_company, name='about_company'),
    path('allspec/', views.AllSpec.as_view()),
    path('contacts/', views.contacts, name='contacts'),
    path('my_notes/', views.my_notes, name='my_notes'),
]
