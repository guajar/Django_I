"""todoro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tasks.views import tasks_list, tasks_detail
from users.views import LoginView, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', tasks_list, name="tasks_list"),  # La URL es /, ejecutar función tasks_list
    url(r'^tasks/(?P<task_pk>[0-9]+)$', tasks_detail, name="tasks_detail"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', logout, name='logout')
]
