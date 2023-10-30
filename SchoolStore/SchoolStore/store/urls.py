from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'store'

urlpatterns = [
    path('', views.allDept, name='allDept'),
    path('course_list/',views.course_list,name="course_list"),
    path('studentDetails/', views.student_Details, name='student_Details'),
    path('studentDetails/add_studDetails', views.add_studDetails, name='add_studDetails'),
    path('<slug:d_slug>/', views.deptDetail, name='course_by_department'),
]
