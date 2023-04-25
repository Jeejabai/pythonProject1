from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.log),
    path('form', views.form),
    path('show', views.show),
    path('read', views.read),
    path('valid', views.valid),
    path('user', views.user),
    path('jee', views.jee),
    path('pro', views.pro,name="pro"),
    path('super', views.super),
    path('product', views.product),
    path('edit/<int:id>/', views.edit,name="edit"),
    path('delete/<int:id>/', views.delete,name="delete"),
    path('logout', views.logout,name="logout"),

]
