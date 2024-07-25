# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, ToDo
from .forms import TaskForm, ToDoForm
import datetime

# def add_task(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         tags = request.POST.get('tags')

#         # Membuat objek Task baru dan menyimpannya ke database
#         Task.objects.create(name=name, priority=priority, tags=tags)
#     return render(request, 'task_list.html')

def add_task(request):
    prty_choices = Task.PRTY_CHOICES

    print(prty_choices, '-------------------')

    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        tags = request.POST.get('tags')
        
        # Simpan data ke model Task
        Task.objects.create(name=name, priority=priority, tags=tags)
        return redirect('task_list')
    
    else:
        form = TaskForm()
    
    context = {
        'form': form,
        'prty_choices': prty_choices
    }
    return render(request, 'task_list.html', context)

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.task = task
            todo.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = ToDoForm()
    
    total_todo = task.todos.count()
    todos_done = task.todos.filter(status='done').count()

    # Hitung persentase
    if total_todo > 0:
        progres = (todos_done / total_todo) * 100
    else:
        progres = 0

    todos_todo = task.todos.filter(status='todo')
    todos_in_progress = task.todos.filter(status='in_progress')
    todos_done = task.todos.filter(status='done')

    # tanggal = datetime.datetime.now().strftime("%A, %d %B %Y") 
    tanggal = datetime.datetime.now().strftime("%A, %d %B %Y").replace("Monday", "Senin").replace("Tuesday", "Selasa").replace("Wednesday", "Rabu").replace("Thursday", "Kamis").replace("Friday", "Jumat").replace("Saturday", "Sabtu").replace("Sunday", "Minggu").replace("January", "Januari").replace("February", "Februari").replace("March", "Maret").replace("April", "April").replace("May", "Mei").replace("June", "Juni").replace("July", "Juli").replace("August", "Agustus").replace("September", "September").replace("October", "Oktober").replace("November", "November").replace("December", "Desember")

    context = {
        'task': task,
        'form': form,
        'todos_todo': todos_todo,
        'todos_in_progress': todos_in_progress,
        'todos_done': todos_done,
        'total_todo': total_todo,
        'progres': progres,
        'tanggal': tanggal,
    }
    
    return render(request, 'task_detail.html', context)

def change_todo_status(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id)
    if todo.status == 'todo':
        todo.status = 'in_progress'
    elif todo.status == 'in_progress':
        todo.status = 'done'
    todo.save()
    return redirect('task_detail', task_id=todo.task.id)
