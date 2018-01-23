from django.db import models
from users.models import Passport
from datetime import datetime


class ChatManager(models.Manager):
	pass


class Chat(models.Model):
	create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
	sender = models.ForeignKey('users.Passport', verbose_name='发送者',related_name='user_sender')
	content = models.CharField(max_length=500, verbose_name='消息内容')
	receiver = models.ForeignKey('users.Passport', verbose_name='接收者')
	objects = ChatManager()
	
	class Meta:
		db_table = 'chats'

