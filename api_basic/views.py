from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Articles, Love
from .serializer import ArticleSerializer, LoveSerializer


# Create your views here.
@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        article = Articles.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def list_love(request):
    if request.method == 'GET':
        love = Love.objects.all()
        serializer = LoveSerializer(love, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LoveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def get_one_love(request, pk):
    try:
        love = Love.objects.get(pk=pk)
    except Love.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LoveSerializer(love)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LoveSerializer(love, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        love.delete()
        return HttpResponse(status=204)
