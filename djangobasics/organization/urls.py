# urls.py
from django.urls import path
from .views import student_list,StudentCreate,StudentUpdate,StudentDelete

urlpatterns = [
    path('studentslist/',student_list.as_view(),name='student_list'),
    path('studentcreate/',StudentCreate.as_view(),name = "student_create"),
    path('studentupdate/<int:pk>/',StudentUpdate.as_view(),name="student_update"),
    path('studentdelete/<int:pk>/',StudentDelete.as_view(),name="student_delete")
]
