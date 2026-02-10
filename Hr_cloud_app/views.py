from django.shortcuts import render

from Hr_cloud_app.forms import HrRegister, LoginRegister


# Create your views here.

def index(request):
    return render(request,'index.html')

def Login(request):
    return render(request,'loginpage.html')

def manager(request):
    return render(request,'manager.html')

def hr(request):
    return render(request,'hr.html')

def employee(request):
    return render(request,'employee.html')

def hr_add(request):

    if request.method == "POST":
        hr_form = HrRegister(request.POST,request.FILES)
        login_form = LoginRegister(request.POST)

        if hr_form.is_valid() and login_form.is_valid():
            hr = login_form.save(commit=False)
            hr.is_Hrm = True
            hr.save()

            user = hr_form.save(commit=False)
            user.Hr_details = hr
            user.save()

        else:
            hr_form = HrRegister()
            login_form = LoginRegister()

            return render(request,"register.html",{'hr_form':hr_form,'login_form':login_form})

