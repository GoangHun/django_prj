from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    age = serializers.CharField(required=False)
    
    class Meta:
        # 직렬화할 모델 설정.
        model = Student
        # 직렬화에 어떤 필드를 포함할지 설정.
        fields = '__all__'