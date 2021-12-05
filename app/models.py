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


class DBApis(models.Model):
    project_id = models.CharField(max_length=10, null=True)  # 项目id
    name = models.CharField(max_length=100, null=True,blank=True)  # 接口名字
    api_method = models.CharField(max_length=10, null=True,blank=True)  # 请求方式
    api_url = models.CharField(max_length=1000, null=True,blank=True)  # url
    api_header = models.CharField(max_length=1000, null=True,blank=True)  # 请求头
    api_login = models.CharField(max_length=10, null=True,blank=True)  # 是否带登陆态
    api_host = models.CharField(max_length=100, null=True,blank=True)  # 域名
    des = models.CharField(max_length=100, null=True,blank=True)  # 描述
    body_method = models.CharField(max_length=20, null=True,blank=True)  # 请求体编码格式
    api_body = models.CharField(max_length=1000, null=True,blank=True)  # 请求体
    result = models.TextField(null=True,blank=True)  # 返回体 因为长度巨大，所以用大文本方式存储
    sign = models.CharField(max_length=10, null=True,blank=True)  # 是否验签
    file_key = models.CharField(max_length=50, null=True,blank=True)  # 文件key
    file_name = models.CharField(max_length=50, null=True,blank=True)  # 文件名
    public_header = models.CharField(max_length=1000, null=True,blank=True)  # 全局变量-请求头

    def __str__(self):
        return self.name
