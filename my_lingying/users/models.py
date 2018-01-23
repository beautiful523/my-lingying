from django.db import models
# 用户表的管理器类(自定义的管理器)
class PassportManager(models.Manager):
	
	# 根据用户名密码查找账户信息的方法
	def get_one_passport(self, user_name):
		passport = self.get(user_name=user_name)
		return passport

# 所有模型的基类
class Passport(models.Model):
	create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
	user_name = models.CharField(max_length=20, verbose_name="用户名")
	job = models.CharField(max_length=50, verbose_name="工作")
	friends = models.ManyToManyField('self') # 好友
	def __str__(self):
		return self.user_name

	# 用户表的管理器实例
	object = PassportManager()
	class Meta:
		# 定义用户表在数据库中的名字
		db_table = "users"
