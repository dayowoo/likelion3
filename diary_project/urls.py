"""diary_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
import diary_app.views
import account.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',diary_app.views.home,name='home'),
    path('new/',diary_app.views.new,name="new"),
    path('create/',diary_app.views.create,name="create"),
    path('update_page/<int:id>',diary_app.views.update_page,name="update_page"),
    path('update/<int:id>',diary_app.views.update,name="update"),
    path('delete/<int:id>',diary_app.views.delete,name="delete"),
    path('account/', include("account.urls")),
    path('like/', include("like.urls")),
    path('search/', diary_app.views.search, name="search"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)