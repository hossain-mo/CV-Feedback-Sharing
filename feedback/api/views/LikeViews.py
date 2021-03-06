from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from feedback.models import Like
from ..serializers import ReadLikeSerializer, WriteLikeSerializer
from rest_framework import status
from django.http import Http404


class LikeList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        likes = Like.objects.all()
        serializer = ReadLikeSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WriteLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, pk):
        try:
            return Like.objects.get(pk=pk)
        except Like.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        like = self.get_object(pk)
        serializer = ReadLikeSerializer(like)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        like = self.get_object(pk)
        serializer = ReadLikeSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cv = self.get_object(pk)
        cv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)