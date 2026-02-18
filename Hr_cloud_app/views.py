from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from Hr_cloud_app.forms import HrRegister, LoginRegister, EmployeeRegister
from Hr_cloud_app.models import Login


def index(request):
    return render(request,'index.html')

def logg(request):
    return render(request,'loginpage.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('manager')

            elif user.is_hr:
                return redirect('hr')

            elif user.is_employee:
                return redirect('employe')

        else:
            messages.info(request, 'Invalid')
    return render(request, 'loginpage.html')

def manager(request):
    return render(request,'manager/manager.html')

def hr(request):
    return render(request,'hr/dashhr.html')

def employe(request):
    return render(request,'employee/dashemp.html')


def hr_add(request):
    if request.method == "POST":
        hrm_form = HrRegister(request.POST, request.FILES)
        login_form = LoginRegister(request.POST)

        if hrm_form.is_valid() and login_form.is_valid():
            hrm = login_form.save(commit=False)
            hrm.is_hr = True
            hrm.save()

            user = hrm_form.save(commit=False)
            user.hr_details = hrm
            user.save()


    else:
            hrm_form = HrRegister()
            login_form = LoginRegister()

    return render(request,'hr/register.html', {'hrm_form': hrm_form, 'login_form': login_form})




def emp_add(request):
    if request.method == "POST":
        emp_form = EmployeeRegister(request.POST, request.FILES)
        login_form = LoginRegister(request.POST)

        if emp_form.is_valid() and login_form.is_valid():
            emp = login_form.save(commit=False)
            emp.is_employee = True
            emp.save()

            user = emp_form.save(commit=False)
            user.employee_details = emp
            user.save()


    else:
        emp_form = EmployeeRegister()
        login_form = LoginRegister()

    return render(request,'employee/register.html', {'emp_form': emp_form, 'login_form': login_form})




