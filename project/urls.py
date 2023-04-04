
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home),
    path('choose/',views.choose),
    # path('plot/', views.plot, name='plot'),
    path('choose/plot2/', views.plot2),
    path('choose/plot3/', views.plot3),
    path('choose/plot4/', views.plot4),
]
