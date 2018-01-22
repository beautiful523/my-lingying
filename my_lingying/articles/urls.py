from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^article/$',article, name='article'), # 获取用户购物车中商品的数量
]