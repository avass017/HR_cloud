from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model


# Create your models here.

class Login(AbstractUser):
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

class Hr(models.Model):
    hr_details =models.OneToOneField("Login",on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField(max_length=100)

class Employee(models.Model):
    employee_details =  models.OneToOneField("Login",on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    department = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    address = models.TextField()


class Work(models.Model):

    work_detail =models.ForeignKey("Employee",on_delete=models.CASCADE)
    work_name = models.CharField(max_length=100)
    work_duration= models.CharField()
    employee_name = models.CharField()
    date = models.DateField()
    status = models.BooleanField(default=False)

    department = (
        ("UI/UX", "Ui/Ux"),
        ("DATA SCIENCE", "data science"),
        ("PYTHON DEVELOPING", "python_developing"),
        ("FLUTTER", "flutter"),
        ("DATA ANALATICS", "data analytics"),
        ("REACT", "react"),
        ("FRONT END DEVELOPING", "front end development"),
        ("BACK END DEVELOPING", "back end development"),
        ("DEVOPS", "devops"),
        ("CLOUD", "cloud"),

    )

    department = models.CharField(max_length=100,
                      choices=department,
                      default="UI/UX")
    def __str__(self):
        return self.work_name


class Payroll(models.Model):
    payroll_details= models.ForeignKey("Employee", on_delete=models.CASCADE)
    salary = models.IntegerField()
    date = models.DateField()

    department = (
        ("UI/UX", "Ui/Ux"),
        ("DATA SCIENCE", "data science"),
        ("PYTHON DEVELOPING", "python_developing"),
        ("FLUTTER", "flutter"),
        ("DATA ANALATICS", "data analytics"),
        ("REACT", "react"),
        ("FRONT END DEVELOPING", "front end development"),
        ("BACK END DEVELOPING", "back end development"),
        ("DEVOPS", "devops"),
        ("CLOUD", "cloud"),

    )

    department = models.CharField(max_length=100,
                                  choices=department,
                                  default="UI/UX")

class Complaint(models.Model):
    complaint_details = models.ForeignKey("Employee", on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    date = models.DateField()



    department = (
        ("UI/UX", "Ui/Ux"),
        ("DATA SCIENCE", "data science"),
        ("PYTHON DEVELOPING", "python_developing"),
        ("FLUTTER", "flutter"),
        ("DATA ANALATICS", "data analytics"),
        ("REACT", "react"),
        ("FRONT END DEVELOPING", "front end development"),
        ("BACK END DEVELOPING", "back end development"),
        ("DEVOPS", "devops"),
        ("CLOUD", "cloud"),

    )
    department = models.CharField(max_length=100,
                                  choices=department,
                                  default="UI/UX")
    status = models.BooleanField(default=False)

class Reply(models.Model):

  subject = models.CharField(max_length=200)
  date = models.DateField()

class Notification(models.Model):
    message= models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)


















