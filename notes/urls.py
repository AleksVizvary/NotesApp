from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_note, name='add_note'),
    path('mark_done/<int:note_id>/', views.mark_done, name='mark_done'),
    ]