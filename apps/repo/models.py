from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.account.models import MyUser
from utils.id_utils import hashid


class FileRepository(models.Model):
    """文件对象"""
    file_type_choices = (
        (1, '文件'),
        (2, '文件夹')
    )
    file_type = models.SmallIntegerField(verbose_name='类型', choices=file_type_choices)
    name = models.CharField(verbose_name='文件夹名称', max_length=32, help_text="文件/文件夹名")
    key = models.CharField(verbose_name='文件存储在COS中的KEY', max_length=128, null=True, blank=True)
    file_size = models.BigIntegerField(verbose_name='文件大小', null=True, blank=True, help_text='字节')
    file_path = models.CharField(verbose_name='文件路径', max_length=255, null=True, blank=True)
    parent = models.ForeignKey(verbose_name='父级目录', to='self', related_name='child', null=True, blank=True,
                               on_delete=models.CASCADE)
    update_user = models.ForeignKey(verbose_name='最近更新者', to=MyUser, on_delete=models.CASCADE)
    update_datetime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        db_table = 'file_repository'
        verbose_name = '文件仓库'
        verbose_name_plural = '文件仓库管理'

    def __str__(self):
        return self.name
