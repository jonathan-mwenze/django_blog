from django.urls import path
from .import views 

urlpatterns = [
   path('',views.index, name="home"),
   path('about/',views.about, name="about"),
   path('skills/',views.skills, name="skills"),
   path('project/',views.project, name="project"),
   path('contact/',views.contact, name="contact"),
]