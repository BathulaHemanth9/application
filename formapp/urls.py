from django.urls import path
from.import views

urlpatterns=[
    path('first/',views.firstform),
    #path('empinsert',views.empinsert)
    path('login/',views.loginuser,name='loginurl'),
    path('logout/',views.logoutuser,name='logouturl'),
    path('signup/',views.signupuser,name='signupurl')
]