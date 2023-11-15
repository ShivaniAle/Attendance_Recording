from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, hod_views,Staff_views,Student_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name = 'base'),
    #login path
    path('',views.LOGIN, name = 'login'),
    path('dologin', views.doLogin, name = 'doLogin'),
    path('dologout', views.doLogout, name = 'logout'),

    # Profile Update
    path('profile',views.PROFILE,name='profile'),

    # This is hod panel url
    path('hod/home' ,hod_views.HOME,name='hod_home'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)