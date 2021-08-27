from django.urls import path
from pdf import views

urlpatterns = [
    path('',views.index1,name='index'),
    path('index1/',views.index1,name='index1'),
    path('login/',views.login,name='login'),
    path('accept',views.accept,name="accept"),
    path('<int:id>/',views.resume,name="resume"),
    path('list/',views.list,name='list'),
    path('notes/',views.notes,name='notes'),
    path('quize/',views.quize,name='quize'),
    path('home/',views.python,name='home'),
    path('java/',views.java,name='java'),
    path('page1/',views.newpage,name='page1'),
    path('choice1/',views.chquize,name='choice1'),
    path('adnotes/',views.adnotes,name='adnotes'),
  
    




]
