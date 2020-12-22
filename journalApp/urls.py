"""journalApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from writing import views
from home.views import (
    home_view,
    note_view,
    titles_view,
    parent_view,
    default_view,

)
from writing.models import notes

    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create', views.create_view.as_view(), name='create'),
    path('', default_view.as_view(), name="default"),
    path('home', home_view.as_view(), name="home"),
    path('note/<int:id>/', note_view.as_view(), name="notes"),
    path('page_created', views.page_created.as_view(), name="page_created"),
    path('titles/<str:parent>/', titles_view.as_view(), name="titles"),
    path('parent', parent_view.as_view(), name="parent")
]
