from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from .form import ToDoForm
from django.http import HttpResponse
from .models import Task

# from .models import Task
# Create your views here.

# class TaskList(ListView):
#     model=Task
    
def homepage(request):
    return render(request,'todoapp/home.html')

def create_todo(request):
    form = ToDoForm()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(create_todo)
        else:
            return HttpResponse('Invalid Todo Data')
            
    context ={'form':form}
    return render(request,'todoapp/createtodo.html',context)


def view_todo(request):
    todo = Task.objects.all().order_by("title")
    context={'todo':todo}
 
        
    return render (request,'todoapp/viewtodo.html',context)


# def edit_todo(request,todo_id):
#     todo = get_object_or_404(Task,id=todo_id)
#     if request.method == 'POST':
#         form = ToDoForm(request.POST,instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect(view_todo)
#     else:
#         form = ToDoForm(instance=todo)   
            
#     return render(request, 'todoapp/edittodo.html',{'form':form})



def edit_todo (request,todo_id):
    task=Task.objects.get(id=todo_id)
    if request.method == "POST":
        form=ToDoForm(request.POST)
        if form.is_valid:
                form.save()
                return redirect('view_todo')
    else:
        form=ToDoForm(instance=task)
        context={"form":form}
    return render(request,"todoapp/createtodo.html",context)   


def todo_details(request,id):
    detail=Task.objects.get(id=id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            todo_id = request.POST.get('delete')
            todo=Task.objects.get(id=todo_id)
            todo.delete()
            return redirect(view_todo)
        elif 'edit' in request.POST:
            todo_id = request.POST.get('edit')
            return redirect('edit_todo',todo_id=todo_id)
    context={"todo_details":detail}
    return render (request,'todoapp/tododetails.html',context)


