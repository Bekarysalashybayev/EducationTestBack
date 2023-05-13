from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions.permissionList import TeacherPermission


class TestApi(APIView):
    permission_classes = [TeacherPermission]

    def get(self, request):
        return Response({'msg': 'OK'})
