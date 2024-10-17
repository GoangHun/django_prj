from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# 각 클래스는 하나의 테이블을 담당(?)
class StudentList(APIView):

    def get(self, request):
        # serializers 파일이 Student를 임포트 하고 있어서 Student의 호출이 가능함.
        # 파이선은 순환 참조 문제가 발생하지 않는다는데 정확한 이해는 못 함.
        model = Student.objects.all()
        serializers = StudentSerializer(model, many=True)
        return Response(serializers.data)