from django.urls import  path
from . import views

urlpatterns= [
    path('',views.iotcoreOverview,name='iotcore-overview'),
    path('switch-list/',views.switchList,name='switch-list'),
    path('switch-detail/<str:pk>/',views.switchDetail,name='switch-detail'),
    path('switch-create/',views.switchCreate,name='switch-create'),
    path('switch-update/<str:pk>/',views.switchUpdate,name='switch-update'),
    path('switch-delete/<str:pk>/',views.switchDelete,name='switch-update'),
]
