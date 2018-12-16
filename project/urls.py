"""project URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers
from miscellaneous.views import MatchViewSet

router = routers.DefaultRouter()



urlpatterns = [

    url(r'^admin/', admin.site.urls),  # admin site
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/v1/', include(router.urls, namespace='api')),

    url(r'^api/web/v1/match/<str:sport>/', MatchViewSet.as_view({'get': 'list'})),
    url(r'^api/web/v1/', include(router.urls, namespace='web')),

    url(r'^api/web/v1/', include('miscellaneous.urls', namespace='miscellaneous')),

]


