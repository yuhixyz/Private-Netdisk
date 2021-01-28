from django.shortcuts import render
from apps.repo.models import FileRepository
from django.http import JsonResponse
from utils.tencent.cos import delete_file, upload_file, create_bucket, credential


def delete_view(request):
    delete_id = request.GET.get('did')
    delete_object = FileRepository.objects.filter(id=delete_id, update_user=request.user).first()
    if delete_object.file_type == 1:  # 删除文件
        pass
        # delete_file(request.user.bucket, )
    else:  # 删除文件夹
        pass

    delete_object.delete()  # 删除数据库中的文件id=delete_id的文件（夹）
    return JsonResponse({'status': True})
