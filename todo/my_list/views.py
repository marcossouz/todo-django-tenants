from django.http import HttpResponse

from .models import MyList


def my_list(request):
    my_list_elements = MyList.objects.all()
    output = ', '.join([q.text for q in my_list_elements])
    return HttpResponse("Lista de tarefas do cliente. -> " + output)
