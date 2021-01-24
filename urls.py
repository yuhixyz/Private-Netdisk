from django.contrib import admin
from django.urls import path
from apps.views import index_view
from apps.account.views import login_view, logout_view
from apps.repo.views import delete_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('delete/', delete_view, name='delete'),
]