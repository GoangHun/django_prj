
from django.urls import path
from test_app.api import StudentList, StudentDetail

urlpatterns = [
    # name은 url 대신 사용.
    path('student_list/', StudentList.as_view(), name='student_list'),
    # <int:student_id>는 StudentDetail에 int형 값을 전달함.
    path('student_list/<int:student_id>', StudentDetail.as_view(), name='student_list'),

]