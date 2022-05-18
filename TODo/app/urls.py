from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add/', views.AddView.as_view(), name='add'),
    path("affairs/", views.get_affairs, name="affairs")
    

]
