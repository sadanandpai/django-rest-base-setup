from django.urls import path
from portal import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('home/', views.home),
    path('fish/', views.fish_list),
    path('fish/<int:pk>/', views.fish_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)