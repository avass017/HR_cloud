from django.urls import path

from Hr_cloud_app import views, hrviews, managerviews, empviews

urlpatterns = [
 path('',views.index,name='index'),
 path('logg',views.logg,name='logg'),
 path('login_view',views.login_view,name='login_view'),
 path('manager',views.manager,name='manager'),
 path('hr',views.hr,name='hr'),
 path('employe',views.employe,name='employe'),
 path('hr_add',views.hr_add,name='hr_add'),
 path('emp_add',views.emp_add,name='emp_add'),


 path('employee_view',hrviews.employee_view,name='employee_view'),
 path('employee_delete/<int:id>',hrviews.employee_delete,name='employee_delete'),
 path('emp_update/<int:id>',hrviews.emp_update,name='emp_update'),
 path('Work_add',hrviews.Work_add,name='Work_add'),


 path('emp_profile/', empviews.emp_profile, name='emp_profile'),

 path('employee_update/<int:id>',empviews.employee_update,name='employee_update'),
 path('work_list',empviews.work_list,name='work_list'),
 path('project_list',hrviews.project_list,name='project_list'),
 path('Project_delete/<int:id>',hrviews.Project_delete,name='Project_delete'),

 path('hr_view',managerviews.hr_view,name='hr_view'),
 path('hr_delete/<int:id>',managerviews.hr_delete,name='hr_delete'),
 path('hr_update/<int:id>',managerviews.hr_update,name='hr_update'),
 path('employes_view',managerviews.employes_view,name='employes_view'),
 path('employee_delete/<int:id>',managerviews.employee_delete,name='employee_delete'),
 path('employee_update/<int:id>',managerviews.employee_update,name='employee_update'),
 path('Start_project/<int:id>',empviews.Start_project,name='Start_project'),

 path('salary_add',hrviews.salary_add,name='salary_add'),
 path('salary_view',hrviews.salary_view,name='salary_view'),
 path('payview',managerviews.payview,name='payview'),
 path('project_view',managerviews.project_view,name='project_view'),
 path('salary_credit',empviews.salary_credit,name='salary_credit'),
 path('complaint_add',empviews.complaint_add,name='complaint_add'),
 path('complaint_view',empviews.complaint_view,name='complaint_view'),
 path('complaint_hr',hrviews.complaint_hr,name='complaint_hr'),
 path('reply_add',hrviews.reply_add,name='reply_add'),
 path('reply_view',hrviews.reply_view,name='reply_view'),
 path('reply_view',empviews.reply_view,name='reply_view'),
 path('noficication',managerviews.noficication,name='noficication'),
 path('send_notification',managerviews.send_notification,name='send_notification'),
 path('complaint_m',managerviews.complaint_m,name='complaint_m'),
 path('noficication_hr',hrviews.noficication_hr,name='noficication_hr'),
 path('overtime',empviews.overtime,name='overtime'),
 path('over_view',empviews.over_view,name='over_view'),
 path('over_view_hr',hrviews.over_view_hr,name='over_view_hr'),
]
