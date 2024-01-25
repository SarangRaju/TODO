from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Tasks
from . forms import todoform
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

class tasklistview(ListView):
    model=Tasks
    template_name='home.html'
    context_object_name='details'

class taskdetailview(DetailView):
    model=Tasks
    template_name = 'details.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model=Tasks
    template_name='edit.html'
    context_object_name = 'task'
    fields=('name','priority','date')
class taskdeleteview(DeleteView):
    model=Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

    def get_success_url(self):
        return reverse_lazy('taskdetailview',kwargs={'pk':self.object.id})
# Create your views here.
def task(request):
    task = Tasks.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        Task=Tasks(name=name,priority=priority,date=date)
        Task.save()

    return render(request,'home.html',{'details':task})
def details(request):
    task = Tasks.objects.all()


    return render(request, 'details.html',{'details':task})
def delete(request,taskid):
    task=Tasks.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,upid):
    task=Tasks.objects.get(id=upid)
    form=todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'form':form,'task':task})


