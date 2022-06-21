from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cont/', views.cont, name='cont'),
    path('one/', views.one, name='one')
]