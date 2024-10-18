from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

# 각 클래스는 하나의 테이블을 담당(?)
class StudentList(APIView):

    def get(self, request):
        # serializers 파일이 Student를 임포트 하고 있어서 Student의 호출이 가능함.
        # 파이선은 순환 참조 문제가 발생하지 않는다는데 정확한 이해는 못 함.
        model = Student.objects.all()
        serializers = StudentSerializer(model, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):
    # student_id는 urls.py에 정의한 대로 url을 통해 전달받음.
    def get(self, request, student_id):
        model = Student.objects.get(student_id=student_id)
        serializers = StudentSerializer(model)
        return Response(serializers.data)
    
    def put(self, request, student_id):
        model = Student.objects.get(student_id = student_id)

        serializer = StudentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, student_id):
        model = Student.objects.get(student_id=student_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
