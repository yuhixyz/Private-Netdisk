from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from utils.id_utils import hashid
from settings.dev import APPID


class MyUser(AbstractUser):
    """
    用户信息
    """
    uid = models.CharField(max_length=32, default='', unique=True, editable=False)  # 具有唯一性的用户ID
    created_at = models.DateTimeField(auto_now_add=True)  # 用户创建的时间
    updated_at = models.DateTimeField(auto_now=True)  # 用户信息最新变更的时间
    region = models.CharField(max_length=32, default='ap-nanjing')
    bucket = models.CharField(max_length=127, default='{}'.format(APPID))

    class Meta:
        db_table = 'user'  # 数据库表名称
        verbose_name = '用户'
        verbose_name_plural = '用户管理'

    def __str__(self):  # 数据库中查询时返回用户名
        return self.username


@receiver(post_save, sender=MyUser, dispatch_uid='gen_user_uid')
def update_uid(sender, instance, **kwargs):
    if not instance.uid:
        instance.uid = hashid(instance.id, length=6)  # 生成用户uid
        instance.save()
