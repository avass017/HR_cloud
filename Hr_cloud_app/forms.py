from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Hr_cloud_app.models import Login, Hr, Employee, Work, Payroll, Complaint, Reply, Notification


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Login

        fields = ('username', 'password1', 'password2')


class HrRegister(forms.ModelForm):
    class Meta:
        model = Hr
        fields = ('name','email','phone','address')

class EmployeeRegister(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name','email','phone','department','address')

class WorkRegister(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }

class PayrollRegister(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }


class ComplaintRegister(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }

class ReplyRegister(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }
class NotificationRegister(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message']

        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter notification message here...'
            }),
        }