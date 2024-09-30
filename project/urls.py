from django.urls import path
from.import views

urlpatterns = [
    path('login/',views.loginuser,name='loginpurl'),
    path('sign/',views.signup,name='signurl'),
    path('logout/',views.logoutuser,name='logouturl'),
]