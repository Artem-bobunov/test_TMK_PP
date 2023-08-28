from . import views
from django.urls import path

urlpatterns = [
    path('', views.list, name='list'),
    path('update/<int:id>', views.update, name='update'),

]
