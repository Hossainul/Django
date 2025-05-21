from django.shortcuts import render,redirect
from .forms import formTask
from .models import AddTask
from .forms import formTask



# Create your views here.
def add_task(req):
    if req.method == "POST":
       form = formTask(req.POST)
       if form.is_valid():
           form.save()
           return redirect('add_task')
    else :
        form = formTask()

    return render(req,'add_task.html',{'form' : form})

def Edit(req,id):
    fetching = AddTask.objects.get(pk = id)
    form_data = formTask(instance=fetching)

    if req.method == 'POST':
        form = formTask(req.POST, instance=fetching)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    else :
        return render(req,'add_categories.html',{'form' : form_data})

def delete(req,id):
    fetching = AddTask.objects.get(pk = id)
    fetching.delete()
    return redirect('homepage')