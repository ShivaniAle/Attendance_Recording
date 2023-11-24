from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, hod_views, staff_views, student_views
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
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    