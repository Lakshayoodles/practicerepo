from django.shortcuts import render
from .forms import StudentListForm
from django.http import HttpResponseRedirect
from .models import studentlist
# Create your views here.


def create_list(request):
    if request.method == "POST":
        form = StudentListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/admin")
    else:
        form = StudentListForm()
    return render(request, "student.html", {"form": form})


def get_list(request):
    students = studentlist.objects.all()
    return render(request, 'studentlist.html', {'students': students})


def update_list(request):
    if request.method == "POST":
        data = request.data.id

def delete_list(request, id):
    student = studentlist.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect("/registration/list")


