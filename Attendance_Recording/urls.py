from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, hod_views, Student_Views, Staff_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name = 'base'),
    #login path
    path('',views.LOGIN, name = 'login'),
    path('dologin', views.doLogin, name = 'doLogin'),
    path('dologout', views.doLogout, name = 'logout'),

    # Profile Update
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE, name = 'profile_update'),


    # This is hod panel url
    path('hod/home' ,hod_views.HOME,name='hod_home'),
    path('hod/Add/Student' ,hod_views.ADD_STUDENT,name='add_student'),
    path('hod/View/Student', hod_views.VIEW_STUDENT, name= "view_student"),
    path('hod/Edit/Student/<str:id>', hod_views.EDIT_STUDENT, name = "edit_student"),
    path('hod/Update/Student' , hod_views.UPDATE_STUDENT, name='update_student'),
    path('hod/Delete/Student/<str:admin>', hod_views.DELETE_STUDENT, name = 'delete_student'),


    path('hod/Add/Staff' ,hod_views.ADD_STAFF,name='add_staff'),
    path('hod/View/Staff' ,hod_views.VIEW_STAFF,name='view_staff'),
    path('hod/Edit/Staff/<str:id>', hod_views.EDIT_STAFF, name = 'edit_staff'),
    path('hod/Update/Staff' , hod_views.UPDATE_STAFF, name = 'update_staff'),
    path('hod/Delete/Staff/<str:admin>' , hod_views.DELETE_STAFF, name = 'delete_staff'),



    path('hod/Add/Course', hod_views.ADD_COURSE, name = 'add_course'),
    path('hod/View/Course', hod_views.VIEW_COURSE, name = 'view_course'),
    path('hod/Edit/Course/<str:id>', hod_views.EDIT_COURSE, name = 'edit_course'),
    path('hod/Update/Course', hod_views.UPDATE_COURSE, name = 'update_course'),
    path('hod/Delete/Course/<str:id>',hod_views.DELETE_COURSE, name='delete_course'),


    path('hod/Add/Subject', hod_views.ADD_SUBJECT, name = 'add_subject'),
    path('hod/View/Subject', hod_views.VIEW_SUBJECT, name = 'view_subject'),
    path('hod/Edit/Subject/<str:id>', hod_views.EDIT_SUBJECT, name = 'edit_subject'),
    path('hod/Update/Subject', hod_views.UPDATE_SUBJECT, name = 'update_subject'),
    path('hod/Delete/Subject/<str:id>',hod_views.DELETE_SUBJECT, name='delete_subject'),

    path('hod/Add/Session', hod_views.ADD_SESSION, name = 'add_session'),
    path('hod/View/Session', hod_views.VIEW_SESSION, name = 'view_session'),
    path('hod/Edit/Session/<str:id>', hod_views.EDIT_SESSION, name = 'edit_session'),
    path('hod/Update/Session', hod_views.UPDATE_SESSION, name = 'update_session'),
    path('hod/Delete/Session/<str:id>',hod_views.DELETE_SESSION, name='delete_session'),

    path('staff/home', Staff_Views.HOME,name = 'staff_home'),
    path('staff/Take_Attendance', Staff_Views.STAFF_TAKE_ATTENDANCE, name = 'staff_take_attendance'),
    path('staff/Save_Attendance', Staff_Views.STAFF_SAVE_ATTENDANCE , name = 'staff_save_attendance'),
    path('staff/View_Attendance', Staff_Views.STAFF_VIEW_ATTENDANCE , name = 'staff_view_attendance'),



    path('student/home', Student_Views.HOME,name = 'student_home'),
    


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    