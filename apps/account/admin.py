from django.contrib import admin
from apps.account.models import MyUser
from apps.repo.models import FileRepository


class FileRepositoryInline(admin.TabularInline):
    """
    将文件仓库内联到用户管理中
    """
    model = FileRepository


class MyUserAdmin(admin.ModelAdmin):
    inlines = [FileRepositoryInline]
    list_display = ('uid', 'username', 'is_active', 'is_staff')


admin.site.register(MyUser, MyUserAdmin)
