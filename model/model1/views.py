from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import StudentListForm
from django.http import HttpResponseRedirect
from .models import studentlist


def create_list(request):
    if request.method == "POST":
        form = StudentListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/data/list")
    else:
        form = StudentListForm()
    return render(request, "student.html", {"form": form})


def get_list(request):
    students = studentlist.objects.all()
    return render(request, 'studentlist.html', {'students': students})


def update_list(request, id):
    obj = get_object_or_404(studentlist, id=id) 
    if request.method == "POST":
        form = StudentListForm(request.POST, instance=obj) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('Student list')) 
    else:
        
        form = StudentListForm(instance=obj) 
    return render(request, 'update_list.html', {'form': form}) 


def delete_list(request, id):
    student = studentlist.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect(reverse('Student list'))
