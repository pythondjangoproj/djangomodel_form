# from django.contrib import admin
from django.urls import path
from . import views

app_name= 'modelform_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', views.Student_info, name='Student_info'),
    path('register/',views.Student_database, name='Student_database'),
    path('api/',views.Student_serialise.as_view(),name='Student_serialise')
]
