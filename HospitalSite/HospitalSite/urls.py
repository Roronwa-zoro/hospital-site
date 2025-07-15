"""
URL configuration for HospitalSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', views.custom_login_view, name='login'),
    path('', views.home, name='home'),
    path('departments/jaw-surgery/', views.jaw_surgery_view, name='jaw_surgery'),
    path('departments/jaw-surgery/monthly-schedule/', views.monthly_schedule_view, name='monthly_schedule'),
    path('departments/jaw-surgery/cold-operations/', views.cold_operations_view, name='cold_operations'),
    path('departments/jaw-surgery/hot-operations/', views.hot_operations_view, name='hot_operations'),

]
urlpatterns+=    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

