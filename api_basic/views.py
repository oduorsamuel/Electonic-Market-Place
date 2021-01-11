from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Articles, Love
from .serializer import ArticleSerializer, LoveSerializer


# Create your views here.
# @csrf_exempt
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article = Articles.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['GET', 'POST'])
def list_love(request):
    if request.method == 'GET':
        love = Love.objects.all()
        serializer = LoveSerializer(love, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = LoveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def get_one_love(request, pk):
    try:
        love = Love.objects.get(pk=pk)
    except Love.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoveSerializer(love)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = LoveSerializer(love, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        love.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
