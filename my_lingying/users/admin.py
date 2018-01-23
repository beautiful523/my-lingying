from django.contrib import admin
from users.models import Passport

class PassportAdmin(admin.ModelAdmin):
	list_display = ['id', 'user_name']

admin.site.register(Passport, PassportAdmin) # 在admin中添加有关账户的编辑功能。

