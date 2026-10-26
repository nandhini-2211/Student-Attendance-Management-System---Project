
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Student management
    path('', views.student_list, name='student_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('student/<int:student_id>/',views.student_detail,name='student_detail'),
    path('export/csv/', views.export_students_csv, name='export_students_csv'),
    path('export/excel/', views.export_students_excel, name='export_students_excel'),
    path('import/', views.import_students, name='import_students'),
    path('users/',views.user_management,name='user_management'),
    path('users/change-role/<int:user_id>/',views.change_user_role,name='change_user_role'),
    path('users/toggle-status/<int:user_id>/',views.toggle_user_status,name='toggle_user_status'),
    path('change-password/',views.change_password,name='change_password'),
    path('password-reset/',auth_views.PasswordResetView.as_view(
        template_name='students/password_reset.html',
        email_template_name='students/password_reset_email.html',
        subject_template_name='students/password_reset_subject.txt',
        success_url='/password-reset/done/'
    ),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(
        template_name='students/password_reset_done.html'
    ),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='students/password_reset_confirm.html',
        success_url='/reset/done/'
    ),name='password_reset_confirm'),
    path('reset/done/',
    auth_views.PasswordResetCompleteView.as_view(
        template_name='students/password_reset_complete.html'
    ),
    name='password_reset_complete'),
    path('verify-email/<uidb64>/<token>/',views.verify_email,name='verify_email'),
    path('attendance/',views.take_attendance,name='take_attendance'),
    path('attendance-history/',views.attendance_history,name='attendance_history'),
    path('export-attendance-excel/',views.export_attendance_excel,name='export_attendance_excel'),
]
