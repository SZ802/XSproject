from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # 请求路径和请求方法
    print(request.path, request.method)
    # 请求头的元信息和GET请求参数（查询参数）
    print(request.META, request.GET)
    print(request.COOKIES)
    # post请求参数（表单参数）
    print(request.POST)
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'art/list.html', context={'name':'disen'})