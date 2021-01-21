from django.contrib import admin
from apps.repo.models import FileRepository


class FileRepositoryAdmin(admin.ModelAdmin):
    """
    后台管理界面中文件仓库展示样式
    """
    list_display = ('file_type', 'name', 'id', 'key', 'file_size', 'file_path', 'parent',
                    'update_user', 'update_datetime')


admin.site.register(FileRepository, FileRepositoryAdmin)
