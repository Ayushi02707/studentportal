from django.urls import path
from to_do_project import views

urlpatterns = [
    path('',views.notes,name="notes")
]