from django.shortcuts import render

from tasks.models import Task


def tasks_list(request):
    """
    Recupera todas las tareas de la BBDD y las pinta
    :param request: objeto HttpRequest
    :return: HttpResponse
    """
    # Recuperar todas las tareas de la BBDD
    tasks = Task.objects.all()

    # Devolver la respuesta
    context = {
        'task_objects': tasks
    }
    return render(request, 'tasks/list.html', context)
