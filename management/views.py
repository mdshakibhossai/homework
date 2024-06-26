from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


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