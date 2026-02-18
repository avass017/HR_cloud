from django.shortcuts import render, redirect

from Hr_cloud_app.forms import EmployeeRegister, WorkRegister, PayrollRegister, ReplyRegister
from Hr_cloud_app.models import Employee, Hr, Work, Payroll, Complaint, Reply


def employee_view(request):
    data = Employee.objects.all()
    return render(request, 'hr/emp_details.html', {"data":data})


def employee_delete(request,id):
    emp_del=Employee.objects.get(id=id)
    emp_del.delete()
    return redirect('employee_view')

def emp_update(request,id):
    emp_up=Employee.objects.get(id=id)

    if request.method == "POST":
        up_form = EmployeeRegister(request.POST,instance=emp_up)
        if up_form.is_valid():
            up_form.save()
            return redirect('employee_view')
    else:
        up_form = EmployeeRegister(instance=emp_up)
    return render(request,'hr/emp_update.html',{'data':up_form})

def Work_add(request):

    if request.method == "POST":
        form = WorkRegister(request.POST)

        if form.is_valid():
            form.save()
            return redirect('project_list')

    else:
        form = WorkRegister()

    return render(request, 'hr/work.html', {'form': form})

def project_list(request):
    data=Work.objects.all()
    return render(request,'hr/work_list.html',{'data':data})

def Project_delete(request,id):
    pro_del=Work.objects.get(id=id)
    pro_del.delete()
    return redirect('project_list')

def salary_add(request):

    if request.method == "POST":
        form = PayrollRegister(request.POST)

        if form.is_valid():
            form.save()
            return redirect('salary_view')

    else:
        form = PayrollRegister()

    return render(request, 'hr/salary.html', {'form': form})

def salary_view(request):
    data=Payroll.objects.all()
    return render(request,'hr/salary_view.html',{'data':data})
def complaint_hr(request):
    data=Complaint.objects.all()
    return render(request,'hr/complaint.html',{'data':data})

def reply_add(request):

    if request.method == "POST":
        form = ReplyRegister(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reply_view')

    else:
        form = ReplyRegister()

    return render(request, 'hr/reply.html', {'form': form})

def reply_view(request):
    data=Reply.objects.all()
    return render(request,'hr/send_reply.html',{'data':data})


