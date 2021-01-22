from django.shortcuts import render
from django.http import JsonResponse
from apps.account.form import LoginForm
from apps.repo.form import DirectoryForm
from apps.repo.models import FileRepository


def index_view(request):
    """
    首页
    """
    parent_object = None
    folder_id = request.GET.get('folder', '')
    if folder_id.isdecimal():
        parent_object = FileRepository.objects.filter(file_type=2, id=int(folder_id)).first()

    if request.method == "GET":
        # 获取当前目录下的文件（夹）
        file_list = []
        if request.user.is_authenticated:
            if parent_object:  # 当前处于parent_object目录
                file_list = FileRepository.objects.filter(update_user=request.user,
                                                          parent=parent_object).order_by('-file_type')
            else:  # 当前处于根目录
                file_list = FileRepository.objects.filter(update_user=request.user,
                                                          parent__isnull=True).order_by('-file_type')

        path = []  # 路径导航条，每个元素为一个字典，表示目录id和目录名称
        parent = parent_object  # 初始化为当前的目录
        while parent:
            path.append({'id': parent.id, 'name': parent.name})
            parent = parent.parent
        path.reverse()

        context = {
            'login_form': LoginForm,  # 登录表单
            'dir_form': DirectoryForm,  # 目录表单
            'file_list': file_list,  # 当前目录下的所有文件（夹）对象
            'parent_object': parent_object,  # 当前目录对象
            'path': path,  # 路径导航条
        }
        return render(request, 'repo/index.html', context)

    # POST

    fid = request.POST.get('fid', '')  # 只有当重命名文件夹时由隐藏input提供
    to_be_renamed = None
    form = None

    if fid.isdecimal():  # 重命名
        to_be_renamed = FileRepository.objects.filter(id=int(fid), update_user=request.user, file_type=2).first()

    if to_be_renamed:  # 当前是需要重命名的文件夹，需要设置instance
        form = DirectoryForm(data=request.POST, instance=to_be_renamed)
    else:
        form = DirectoryForm(data=request.POST)

    if form.is_valid():
        form.instance.file_type = 2
        form.instance.update_user = request.user
        form.instance.parent = parent_object
        form.save()
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors})
