from django.shortcuts import render


def index(request):
	# 使用模板
	return render(request, 'index.html', locals())