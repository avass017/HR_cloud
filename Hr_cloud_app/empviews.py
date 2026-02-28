from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.utils import timezone

from Hr_cloud_app.forms import EmployeeRegister, ComplaintRegister, OvertimeRegister, LeaveRegister
from Hr_cloud_app.models import Employee, Work, Payroll, Complaint, Reply, Overtime, Leave

from django.shortcuts import render
from .models import Employee

def emp_profile(request):

    employee = Employee.objects.first()   # just get first employee

    return render(request, 'employee/emp_profile.html', {'data': employee})



def profile_update(request,id):

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
    project.status = True
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
            complaint = form.save(commit=False)
            complaint.complaint_details = request.user.employee  # assign employee
            complaint.date = timezone.localdate()  # assign today's date
            complaint.save()
            return redirect('complaint_view')
    else:
        form = ComplaintRegister()

    return render(request, 'employee/complaint.html', {'form': form})

def complaint_view(request):
    employee = request.user.employee
    data = Complaint.objects.filter(complaint_details=employee)
    return render(request, 'employee/complaint_view.html', {'data': data})

def reply_view_e(request):
    employee = Employee.objects.get(employee_details=request.user)
    data = Reply.objects.filter(reply_details=employee)
    return render(request, 'employee/complaint_reply.html', {'data': data})

 

def overtime(request):

    if request.method == "POST":
        form = OvertimeRegister(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.employee = Employee.objects.get(employee_details=request.user)
            obj.save()
            return redirect('over_view')

    else:
        form = OvertimeRegister()

    return render(request, 'employee/overtime.html', {'form': form})





def over_view(request):
    employee = Employee.objects.get(employee_details=request.user)
    data = Overtime.objects.filter(employee=employee)
    return render(request,'employee/over_view.html',{'data':data})


def leave_add(request):

    employee = Employee.objects.get(employee_details=request.user)

    if request.method == "POST":
        form = LeaveRegister(request.POST)

        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = employee   # 👈 attach employee
            leave.save()
            return redirect('leave_view')

    else:
        form = LeaveRegister()

    return render(request, 'employee/leave_add.html', {'form': form})



def leave_view(request):
    employee = Employee.objects.get(employee_details=request.user)
    data = Leave.objects.filter(employee=employee)
    return render(request,'employee/leave_list.html',{'data':data})

def Log_out(request):
    logout(request)
    return redirect('login_view')

def employee_dashboard(request):

    employee = Employee.objects.get(employee_details=request.user)

    total_projects = Work.objects.count()
    active_projects = Work.objects.filter(status=True).count()
    total_complaints = Complaint.objects.filter(complaint_details=employee).count()
    total_overtime = Overtime.objects.filter(employee=employee).count()
    total_leave = Leave.objects.filter(employee=employee).count()
    salary_count = Payroll.objects.filter(payroll_details=employee).count()

    context = {
        'employee': employee,
        'total_projects': total_projects,
        'active_projects': active_projects,
        'total_complaints': total_complaints,
        'total_overtime': total_overtime,
        'total_leave': total_leave,
        'salary_count': salary_count,
    }

    return render(request, 'employee/dashboard.html', context)