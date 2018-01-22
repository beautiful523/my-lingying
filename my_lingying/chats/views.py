from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from chats.models import Chat
# from books.models import Books
from users.models import Passport
import json
import time
from django.db.models import Q


@csrf_exempt
def chat(request):
	if request.method == "GET":
		# 从数据库获取动态
		chats = Chat.objects.filter(Q(sender=2, receiver=1)|Q(sender=1, receiver=2))
		data = []
		for c in chats:
			sender_id = c.sender_id
			data.append({
				'sender_id': sender_id,
				'create_time':c.create_time,
				'content': c.content
			})
		res = {
			'code': 200,
			'data': data,
		}
		return JsonResponse(res)

	else:
		# ajax像数据库上传动态
		params = json.loads(request.body.decode('utf-8'))
		content = params.get('content')
		print(content)
		sender = Passport.object.get(id=2)
		receiver = Passport.object.get(id=1)
		chat = Chat(sender=sender,content=content,receiver=receiver,create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		chat.save()
		# Article.objects.create(passport_id=2,content=content)
		# return HttpResponse('{"status": "200"}', content_type='application/json')
		return JsonResponse({
			'code': 200,
			'msg': '评论成功',
		})