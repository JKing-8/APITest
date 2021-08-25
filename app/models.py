from django.db import models


# Create your models here.
# 吐槽内容
class DBFeedback(models.Model):
    user = models.CharField(max_length=20, null=True)
    text = models.CharField(max_length=20, null=True)
    ctime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + str(self.ctime)
