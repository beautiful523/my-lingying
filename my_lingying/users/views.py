from django.shortcuts import render


def index(request):
	# 使用模板
	return render(request, 'users/index.html', locals())


def messaging(request):
	return render(request, 'chats/messaging.html', locals())