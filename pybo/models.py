from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    PUBLIC_METHOD_CHOICES = [
        ('time', '時刻公開'),
        ('immediate', 'すぐ公開'),
        ('hold', '保留'),
    ]
    public_method = models.CharField(
        max_length=20,
        choices=PUBLIC_METHOD_CHOICES,
        default='time'
    )
    PUSH_CHOICES = [
        ('push-on', '通知する'),
        ('push-off', '通知しない'),
    ]
    push = models.CharField(
        max_length=20,
        choices=PUSH_CHOICES,
        default='push-on'
    )
    issued_date = models.DateTimeField()
    expiry_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'pybo_table'

    def __str__(self):
        return self.subject

    def get_push_display(self):
        return dict(self.PUSH_CHOICES).get(self.push)

    def get_public_display(self):
        return dict(self.PUBLIC_METHOD_CHOICES).get(self.public_method)