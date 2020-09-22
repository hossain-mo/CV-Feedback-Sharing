from rest_framework import serializers
from ..models import Cv, Comment, Follow, Like
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    is_superuser = serializers.BooleanField(required=False)
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    is_staff = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False, default=1)
    date_joined = serializers.DateTimeField(required=False)

    class Meta:
        model = User
        exclude = ["password", "last_login"]


class ReadCvSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Cv
        exclude = ["updated_date"]


class WriteCvSerializer(serializers.ModelSerializer):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        model = Cv
        exclude = ["updated_date"]


class ReadCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    cv = serializers.StringRelatedField()
    content = serializers.CharField(required=True)

    class Meta:
        model = Comment
        exclude = ["updated_date"]


class WriteCommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)

    class Meta:
        model = Comment
        exclude = ["updated_date"]


class ReadLikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    cv = serializers.StringRelatedField()
    creation_date = serializers.DateTimeField()

    class Meta:
        model = Like
        fields = '__all__'


class WriteLikeSerializer(serializers.ModelSerializer):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)

    class Meta:
        model = Like
        exclude = ['creation_date']


class ReadFollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    followed_user = serializers.StringRelatedField()
    creation_date = serializers.DateTimeField()

    class Meta:
        model = Follow
        fields = '__all__'


class WriteFollowSerializer(serializers.ModelSerializer):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followed_user = models.ForeignKey(Cv, on_delete=models.CASCADE)

    class Meta:
        model = Follow
        exclude = ['creation_date']

