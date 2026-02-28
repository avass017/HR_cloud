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
 path('empl_update/<int:id>',hrviews.empl_update,name='empl_update'),
 path('Work_add',hrviews.Work_add,name='Work_add'),


 path('emp_profile/', empviews.emp_profile, name='emp_profile'),

    path('profile_update/<int:id>/', empviews.profile_update, name='profile_update'),
    path('work_list',empviews.work_list,name='work_list'),
 path('project_list',hrviews.project_list,name='project_list'),
 path('Project_delete/<int:id>',hrviews.Project_delete,name='Project_delete'),

 path('hr_view',managerviews.hr_view,name='hr_view'),
 path('hr_delete/<int:id>',managerviews.hr_delete,name='hr_delete'),
 path('hr_update/<int:id>',managerviews.hr_update,name='hr_update'),
 path('employes_view',managerviews.employes_view,name='employes_view'),
 path('employee_delete/<int:id>',managerviews.employee_delete,name='employee_delete'),
 path('emp_update/<int:id>',managerviews.emp_update,name='emp_update'),
 path('Start_project/<int:id>',empviews.Start_project,name='Start_project'),

 path('salary_add',hrviews.salary_add,name='salary_add'),
 path('salary_view',hrviews.salary_view,name='salary_view'),
 path('payview',managerviews.payview,name='payview'),
 path('project_view',managerviews.project_view,name='project_view'),
 path('salary_credit',empviews.salary_credit,name='salary_credit'),
 path('complaint_add',empviews.complaint_add,name='complaint_add'),
 path('complaint_view',empviews.complaint_view,name='complaint_view'),
 path('complaint_hr',hrviews.complaint_hr,name='complaint_hr'),
 path('reply_add/<int:id>/', hrviews.reply_add, name='reply_add'),
 path('reply_view_hr/<int:id>',hrviews.reply_view_hr,name='reply_view_hr'),
 path('reply_view_e',empviews.reply_view_e,name='reply_view_e'),
 path('noficication',managerviews.noficication,name='noficication'),
 path('send_notification',managerviews.send_notification,name='send_notification'),
 path('complaint_m',managerviews.complaint_m,name='complaint_m'),
 path('noficication_hr',hrviews.noficication_hr,name='noficication_hr'),
 path('overtime',empviews.overtime,name='overtime'),
 path('over_view',empviews.over_view,name='over_view'),
 path('over_view_hr',hrviews.over_view_hr,name='over_view_hr'),
# Employee
 path('leave_add',empviews.leave_add,name='leave_add'),
 path('leave_view', empviews.leave_view, name='leave_view'),

# HR
path('leave_view_hr/', hrviews.leave_view_hr, name='leave_view_hr'),
path('accept_leave/<int:id>/', hrviews.accept_leave, name='accept_leave'),
path('reject_leave/<int:id>/', hrviews.reject_leave, name='reject_leave'),
path('Log_out',empviews.Log_out,name='Log_out'),
path('Log_out_m',managerviews.Log_out_m,name='Log_out_m'),
path('Log_out_hr',hrviews.Log_out_hr, name='Log_out_hr'),

]
