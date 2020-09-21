from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()
    creation_date = models.DateTimeField("date created", auto_now_add=True)
    updated_date = models.DateTimeField("date updated", auto_now=True)

    def __str__(self):
        return self.file.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date created", auto_now_add=True)
    updated_date = models.DateTimeField("date updated", auto_now=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    creation_date = models.DateTimeField("date created", auto_now_add=True)

    class Meta:
        unique_together = ('user', 'cv')


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_user_id')
    creation_date = models.DateTimeField("date created", auto_now_add=True)

    class Meta:
        unique_together = ('user', 'followed_user')
