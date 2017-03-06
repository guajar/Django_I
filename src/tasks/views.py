from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from tasks.models import Task


@login_required()
def tasks_list(request):
    """
    Recupera todas las tareas de la BBDD y las pinta
    :param request: objeto HttpRequest
    :return: HttpResponse
    """

    # Recuperar todas las tareas de la BBDD
    tasks = Task.objects.select_related("owner", "assignee").all()

    # Comprobamos si se debe flitrar por tareas creadas por el user autenticado
    if request.GET.get('filter') == 'owned':
        tasks = tasks.filter(owner=request.user)

    # Comprobamos si se debe flitrar por tareas creadas por el user autenticado
    if request.GET.get('filter') == 'assigned':
        tasks = tasks.filter(assignee=request.user)

    # Devolver la respuesta
    context = {
        'task_objects': tasks
    }
    return render(request, 'tasks/list.html', context)


@login_required()
def tasks_detail(request, task_pk):
    """
    Recupera una tarea de la BBDD y la pinta con una plantilla
    :param request: HttpRequest
    :param task_pk: Primary key de la tarea a recuperar
    :return: HttpResponse
    """

    # Recuperar la tarea
    # Opción 1
    try:
        task = Task.objects.select_related().get(pk=task_pk)
    except Task.DoesNotExist:
        return render(request, '404.html', status=404)
    except Task.MultipleObjectsReturned:
        return HttpResponse("Existen varias tareas con ese identificador", status=300)

    # Preparar el contexto
    context = {
        'task': task
    }

    # Renderizar la plantilla
    return render(request, 'tasks/detail.html', context)
