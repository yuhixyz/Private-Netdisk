from django.shortcuts import render
from apps.repo.models import FileRepository
from django.http import JsonResponse
from utils.tencent.cos import delete_file, delete_file_list, upload_file, create_bucket, get_credential


def delete_view(request):
    """
    删除文件（夹）
    """
    delete_id = request.GET.get('did')
    delete_object = FileRepository.objects.filter(id=delete_id, update_user=request.user).first()
    if delete_object.file_type == 1:  # 删除文件
        # cos中删除文件
        delete_file(bucket=request.user.bucket, region=request.user.region, key=delete_object.key)
        # 数据库中删除文件
        delete_object.delete()
    else:  # 删除文件夹
        # 设置一个队列q，bfs删除文件(夹)
        q = [delete_object]
        hh, tt = 0, 0
        key_list = []  # 待删除的文件列表，每个元素的格式为 {'Key': key}
        while hh <= tt:  # 当q不空
            # 取出队头文件夹
            t = q[hh]
            hh += 1
            # 遍历t下的所有文件（夹）
            file_list = FileRepository.objects.filter(update_user=request.user, parent=t)
            for file in file_list:
                if file.file_type == 1:  # file是文件
                    key_list.append({'Key': file.key})
                else:  # file是文件夹
                    q.append(file)
                    tt += 1

        if key_list:
            # cos批量删除文件
            delete_file_list(bucket=request.user.bucket, region=request.user.region, key_list=key_list)
        # 在数据库中删除文件夹
        delete_object.delete()

    return JsonResponse({'status': True})


def credential_view(request):
    """
    返回临时凭证
    """
    data_dict = get_credential(request.user.bucket, request.user.region)
    return JsonResponse({'status': True, 'data': data_dict})


def file_save_view(request):
    """
    文件上传成功后写入数据库
    """
    # print(request.POST)
    name = request.POST.get('name')
    file_size = request.POST.get('file_size')
    key = request.POST.get('key')
    parent_id = request.POST.get('parent_id', '')
    file_type = 1
    update_user = request.user
    parent = None
    if parent_id.isdecimal():
        parent = FileRepository.objects.filter(update_user=request.user, id=parent_id).first()
    file_path = request.POST.get('file_path')

    # 在数据库中创建该文件对象
    res = FileRepository.objects.create(file_type=file_type, file_path=file_path, name=name, file_size=file_size, key=key,
                                  parent=parent, update_user=update_user)

    dict = {
        'id': res.id,
        'name': name,
        'file_size': file_size,
        'update_user': update_user.username,
        'file_path': file_path,
        'update_datetime': res.update_datetime.strftime('%Y{y}%m{m}%d{d} %H:%M').format(y='年',m='月',d='日'),
    }
    return JsonResponse({'status': True, 'data': dict})
