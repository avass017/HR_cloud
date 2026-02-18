from django.shortcuts import render, redirect

from Hr_cloud_app.forms import EmployeeRegister, ComplaintRegister, OvertimeRegister
from Hr_cloud_app.models import Employee, Work, Payroll, Complaint, Reply, Overtime

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


def salary_credit(request):
    employee=Employee.objects.get(employee_details=request.user)
    data = Payroll.objects.filter(payroll_details=employee)

    return render(request,'employee/salary.html',{'data':data})

def complaint_add(request):

    if request.method == "POST":
        form = ComplaintRegister(request.POST)

        if form.is_valid():
            form.save()
            return redirect('complaint_view')

    else:
        form = ComplaintRegister()

    return render(request, 'employee/complaint.html', {'form': form})

def complaint_view(request):
    employee = Employee.objects.get(employee_details=request.user)
    data = Complaint.objects.filter(complaint_details=employee)
    return render(request,'employee/complaint_view.html',{'data':data})

def reply_view(request):
    employee = Employee.objects.get(employee_details=request.user)
    data = Reply.objects.filter(complaint_details=employee)
    return render(request,'employee/complaint_reply.html',{'data':data})


def overtime(request):

    if request.method == "POST":
       form = OvertimeRegister(request.POST)

       if form.is_valid():
        form.save()
        return redirect('over_view')

    else:
        form = OvertimeRegister()

    return render(request, 'employee/overtime.html', {'form': form})

def over_view(request):
    employee = Employee.objects.get(employee_details=request.user)
    data = Overtime.objects.filter(employee=employee)
    return render(request,'employee/overview.html',{'data':data})