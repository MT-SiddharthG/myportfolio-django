from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/',    views.ProjectsView.as_view(),    name='projects'),
    path('experience/',  views.ExperienceView.as_view(),  name='experience'),
    path('contact/',     views.ContactView.as_view(),     name='contact'),
]
