# 本文件是本地开发阶段所使用的配置文件，注意修改 manage.py 和 wsgi.py 的配置文件
# 请将如下密钥都替换后再将 dev.example.py 修改为 dev.py

from .base import *

# （覆盖 base.py 中的配置项）请替换掉如下密钥（本人均已替换）
SECRET_KEY = '&)+ox*a-3v0kzud=628lrp5-(u=s2nsm%b@+on@*fx#j$5i!f^'

# 请用腾讯云COS密钥进行替换（本人均已替换）
COS_SECRET_ID = 'AKIDe7ML3TmhRAXgbGJg0ShXBerVv4wTIMhp'
COS_SECRET_KEY = 'DDzWj3EC0bz7zOzMagvxhBoh3A1dswnw'
APPID = '1304853137'