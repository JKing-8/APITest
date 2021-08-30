from django.db import models


# Create your models here.
# 吐槽内容
class DBFeedback(models.Model):
    user = models.CharField(max_length=20, null=True)
    text = models.CharField(max_length=20, null=True)
    ctime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + str(self.ctime)


class DBLinkAll(models.Model):
    name = models.CharField(max_length=100, null=True)
    href = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class DBProject(models.Model):
    name = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=1000, null=True)
    user = models.CharField(max_length=50, null=True)
    other_user = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
