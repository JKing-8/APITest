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
    name = models.CharField(max_length=100, null=True)  # 项目名字
    remark = models.CharField(max_length=1000, null=True)  # 项目备注
    user = models.CharField(max_length=15, null=True)  # 项目创建者名字
    user_id = models.CharField(max_length=10, null=True)  # 项目创建者id
    other_user = models.CharField(max_length=200, null=True, blank=False)  # 项目其他创建者
    global_datas = models.CharField(max_length=100, null=True, blank=False)  # 所生效的变量组的id列表

    def __str__(self):
        return self.name

