# 本文件是线上部署阶段所使用的配置文件，注意修改 manage.py 和 wsgi.py 的配置文件
# 请根据 dev.py 中的内容对应修改线上部署时的配置，然后将 prod.example.py 修改为 prod.py

from .base import *


DEBUG = False