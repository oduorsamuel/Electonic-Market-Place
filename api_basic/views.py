from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Articles, Love
from .serializer import ArticleSerializer, LoveSerializer
from rest_framework.views import APIView


# Create your views here.
# //Generic api views
class Generic(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
              mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = LoveSerializer
    queryset = Love.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# class bassed views
class LoveData(APIView):
    def get(self, request):
        love = Love.objects.all()
        serializer = LoveSerializer(love, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    def post(self, request):
        serializer = LoveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LoveDetails(APIView):
    def get_object(self, pk):
        try:
            return Love.objects.get(pk=pk)
        except Love.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        love = self.get_object(pk)
        serializer = LoveSerializer(love)
        return Response(serializer.data)

    def put(self, request, pk):
        love = self.get_object(pk)
        serializer = LoveSerializer(love, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        love = self.get_object(pk)
        love.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Function based views
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        love.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
