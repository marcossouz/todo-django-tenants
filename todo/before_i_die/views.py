from django.http import HttpResponse

from before_i_die.models import BeforeIDie


def before_i_die(request):
    list_elements = BeforeIDie.objects.all()
    output = ', '.join([q.text for q in list_elements])
    return HttpResponse("Lista global de coisas para fazer antes de morrer. -> " + output)
