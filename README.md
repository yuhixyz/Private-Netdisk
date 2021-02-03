## 私有网盘
   
   本项目采用 `django`，`semantic-ui`，腾讯云对象存储实现了一个私人网盘。

   本地测试需要注册腾讯云的对象存储服务，并在 settings/dev.py 中配置相关信息。

## 环境配置

1. 下载

    ```
    git clone git@github.com:yuhixyz/Private-Netdisk.git
    cd Private-Netdisk
    ```

2. 安装依赖（python>=3.7.9）

    进入项目根目录，然后安装项目的依赖
    
    ```
    pip install -r requirements.txt
    ```

## 启动本地服务

1. 将 settings 下的 dev.example.py 修改为 dev.py 并修改其中的配置项（参见注释说明）

2. 建立数据库（使用 sqlite3，无需额外配置，如果需要配置其他数据库，请在 dev.py 中覆盖 base.py 中的数据库配置）
    
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

2. 拷贝静态文件
    
    ```
    python manage.py collectstatic
    ```

3. 创建超级管理员

    ```
    python manage.py createsuperuser
    ```

4. 启动本地服务

    ```
    python manage.py runserver
    ```

    访问 http://127.0.0.1:8000 。

    注意：此时使用的配置为 settings.dev 。如果需要线上部署，请将配置文件切换为 settings.prod （需要修改 manage.py 和 wsgi.py 中的配置）。

5. 登录 django-admin 后台
    
    访问 http://127.0.0.1:8000/admin 。

6. 登录后台后创建其他用户

    用户名：随便取； 密码：xxx

    在命令行，用 `python manage.py shell` 进入交互状态（注意不要直接使用 `python` 命令进入交互模式， django 会找不到 DJANGO_SETTINGS_MODULE 这一配置信息）

    进入交互状态后，利用 `make_password()` 生成密码即可。

    假设你需要生成的密码是 tqlqwqtql，那么按照如下方式：

    ```python
    from django.contrib.auth.hashers import make_password 
    print(make_password('tqlqwqtql'))
    ```

    得到的结果就是管理员需要在后台预置的密码，用户登陆时，使用密码 tqlqwqtql 登录即可。
