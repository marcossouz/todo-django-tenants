from django.http import HttpResponse

from rest_framework import viewsets

from .models import BeforeIDie
from .serializers import BeforeIDieSerializer


def before_i_die(request):
    list_elements = BeforeIDie.objects.all()
    output = ', '.join([q.text for q in list_elements])
    return HttpResponse("Lista global de coisas para fazer antes de morrer. -> " + output)


class BeforeIDieViewSet(viewsets.ModelViewSet):
    queryset = BeforeIDie.objects.all()
    serializer_class = BeforeIDieSerializer
