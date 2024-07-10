from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from .pagination import *


@api_view(['GET'])
def index(request):
    person1 = {
        "name":"shakib",
        "age":18,
        "is_marride":False,
    }
    person2 = {
        "name":"ratul",
        "age":19,
        "is_marride":False
    }

    person_list = [person1,person2]
    return Response(person_list,)


@api_view(['GET','POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        
        paginator = TodoPagination()
        page = paginator.paginate_queryset(todos, request)

        if page is not None:
            serializer = TodoListSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)


        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        data = request.data
        serializer = TodoCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save(create_by = request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','DELETE'])
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'GET':
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        todo.delete()
        massage = {"success":"Todo has been delete successfully"}
        return Response(massage,status=status.HTTP_204_NO_CONTENT)