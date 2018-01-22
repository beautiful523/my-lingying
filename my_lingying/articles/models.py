from django.db import models
from users.models import Passport
from datetime import datetime

class ArticleManager(models.Manager):
	pass

class Article(models.Model):
	create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
	passport = models.ForeignKey('users.Passport',verbose_name='发动态者')
	content = models.CharField(max_length=500, verbose_name='动态内容')
	
	objects = ArticleManager()
	class Meta:
		db_table = 'articles'
		
		