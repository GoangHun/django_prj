
from django.contrib import admin
from django.urls import path, include

from test_app.api import StudentList, StudentDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    # name은 url 대신 사용.
    path('api/', include('test_app.urls')),
]
