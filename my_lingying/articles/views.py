from django.http import HttpResponse
from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from articles.models import Article
# from books.models import Books
from users.models import Passport
import json
# import redis
import time
@csrf_exempt
def article(request):
	if request.method == "GET":
		# 从数据库获取动态
		articles = Article.objects.all()
		articles = articles[::-1]
		data = []
		for c in articles:
			passport_id = c.passport_id
			passport = Passport.object.get(id=passport_id)

			data.append({
				'user_name': passport.user_name,
				'job':passport.job,
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
		# user_id = params.get('user_id')
		content = params.get('content')
		print(content)
		passport = Passport.object.get(id=2)
		article = Article(passport=passport,content=content,create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		article.save()
		# Article.objects.create(passport_id=2,content=content)
		# return HttpResponse('{"status": "200"}', content_type='application/json')
		return JsonResponse({
			'code': 200,
			'msg': '评论成功',
		})