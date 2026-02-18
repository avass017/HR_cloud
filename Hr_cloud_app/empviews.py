from django.shortcuts import render, redirect

from Hr_cloud_app.forms import EmployeeRegister
from Hr_cloud_app.models import Employee, Work


from django.shortcuts import render
from .models import Employee

def emp_profile(request):

    employee = Employee.objects.first()   # just get first employee

    return render(request, 'employee/emp_profile.html', {'employee': employee})



def employee_update(request, id):
    emp_up = Employee.objects.get(id=id)

    if request.method == "POST":
        up_form = EmployeeRegister(request.POST, instance=emp_up)
        if up_form.is_valid():
            up_form.save()
            return redirect('emp_profile')
    else:
        up_form = EmployeeRegister(instance=emp_up)
    return render(request, 'employee/emplo_update.html', {'data': up_form})


def work_list(request):
    data=Work.objects.all()
    return render(request,'employee/work_list.html',{'data':data})

def Start_project(request, id):
    project = Work.objects.get(id=id)
    project.status = 'started'
    project.save()
    return redirect('work_list')



