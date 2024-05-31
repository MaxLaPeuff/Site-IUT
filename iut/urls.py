
from django.urls import path
from . import views
from .views import List


urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('administration',views.administration,name='administration'),
    path('detail/<slug:slug>',views.detailView,name='detailView'),
    path('home', List.as_view(), name='home'),
    path('memoire',views.memoire_list,name='memoire_list'),
    path('contacter',views.contacter,name='contacter'),
    path('personnel', views.personnel, name='personnel'),

    
]


