from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Hr_cloud_app.forms import HrRegister, EmployeeRegister, NotificationRegister
from Hr_cloud_app.models import Hr, Employee, Payroll, Work, Notification, Complaint


def hr_view(request):
    data = Hr.objects.all()
    return render(request, 'manager/hrviews.html', {"data":data})

def employes_view(request):
    data = Employee.objects.all()
    return render(request, 'manager/empview.html', {"data":data})

def employee_delete(request,id):
    emp_del=Employee.objects.get(id=id)
    emp_del.delete()
    return redirect('employee_view')

def employee_update(request, id):
    emp_up = Employee.objects.get(id=id)

    if request.method == "POST":
        up_form = EmployeeRegister(request.POST, instance=emp_up)
        if up_form.is_valid():
            up_form.save()
            return redirect('empiew')
    else:
        up_form = EmployeeRegister(instance=emp_up)
    return render(request, 'manager/emp_update.html', {'data': up_form})


def hr_delete(request,id):
    hr_del=Hr.objects.get(id=id)
    hr_del.delete()
    return redirect('hr_view')

def hr_update(request,id):
    hr_up=Hr.objects.get(id=id)

    if request.method == "POST":
        up_form = HrRegister(request.POST,instance=hr_up)
        if up_form.is_valid():
            up_form.save()
            return redirect('hrview')
    else:
        up_form = HrRegister(instance=hr_up)
    return render(request,'manager/hr_update.html',{'data':up_form})

def payview(request):
    data=Payroll.objects.all()
    return render(request,'manager/payroll_c.html',{'data':data})

def project_view(request):
    data=Work.objects.all()
    return render(request,'manager/worklist.html',{'data':data})

def send_notification(request):
    form = NotificationRegister()

    if request.method == "POST":
        form = NotificationRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noficication')

    return render(request, 'manager/notification_add.html', {'form': form})

def noficication(request):
    data=Notification.objects.all()
    return render(request,'manager/notifications.html',{'data':data})

def complaint_m(request):
    data=Complaint.objects.all()
    return render(request,'manager/complaint_manager.html',{'data':data})
