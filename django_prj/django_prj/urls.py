
from django.contrib import admin
from django.urls import path

from test_app.api import StudentList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student_list', StudentList.as_view(), name='student_list')
]
