from django.http import JsonResponse
from django.shortcuts import render
from .forms import TaskForm
from .models import Task
from django.views.decorators.csrf import csrf_exempt


def home(request):
    form = TaskForm()
    tasks = Task.objects.all()
    context = {'form': form, 'tasks': tasks}
    return render(request, 'crud/home.html', context)


def task_detail(request, id):
    task = Task.objects.get(pk=id)
    return render(request, 'crud/task_detail.html', {'task': task})


@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            tid = request.POST.get('taskid')
            name = request.POST['name']
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            status = request.POST['status']

            if (tid == ''):
                task = Task(name=name, start_date=start_date,
                            end_date=end_date, status=status)
            else:
                task = Task(id=tid, name=name, start_date=start_date,
                            end_date=end_date, status=status)
            task.save()

            tasks = Task.objects.values()
            task_data = list(tasks)

            return JsonResponse({'status': 'Data Saved', 'task_data': task_data})
        else:
            return JsonResponse({'status': 'Not Saved'})


@csrf_exempt
def delete_task(request):
    if request.method == 'POST':
        id = request.POST.get('tid')
        task = Task.objects.get(pk=id)
        task.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


@csrf_exempt
def update_task(request):
    if request.method == 'POST':
        id = request.POST.get('tid')
        task = Task.objects.get(pk=id)
        task_data = {'id': task.id, 'name': task.name, 'start_date': task.start_date,
                     'end_date': task.end_date, 'status': task.status}
        return JsonResponse(task_data)
