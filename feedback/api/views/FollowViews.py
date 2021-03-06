from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from feedback.models import Follow
from ..serializers import ReadFollowSerializer, WriteFollowSerializer
from rest_framework import status
from django.http import Http404


class FollowList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        follows = Follow.objects.all()
        serializer = ReadFollowSerializer(follows, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WriteFollowSerializer(data=request.data)

        if serializer.is_valid():
            if serializer.data['user'] is serializer.data['followed_user']:
                return Response({"message":"user can't follow himself"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, pk):
        try:
            return Follow.objects.get(pk=pk)
        except Follow.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        follow = self.get_object(pk)
        serializer = ReadFollowSerializer(follow)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        follow = self.get_object(pk)
        serializer = ReadFollowSerializer(follow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cv = self.get_object(pk)
        cv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)