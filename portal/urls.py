from django.urls import path
from django.conf.urls import url, include
from portal import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('home/', views.home),
]

urlpatterns = format_suffix_patterns(urlpatterns)