from django.http import HttpResponse

from rest_framework import viewsets

from .models import MyList
from .serializers import MyListSerializer


def my_list(request):
    my_list_elements = MyList.objects.all()
    output = ', '.join([q.text for q in my_list_elements])
    return HttpResponse("Lista de tarefas do cliente. -> " + output)


class MyListViewSet(viewsets.ModelViewSet):
    queryset = MyList.objects.all()
    serializer_class = MyListSerializer
