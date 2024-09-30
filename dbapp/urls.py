from django.urls import path
from.import views

urlpatterns=[
    path('',views.dbprocess),
    path('insert/',views.dbinsert,name='insertemployeeurl'),
    path('select/',views.dbselect,name='selectemployeeurl'),
    path('update/<int:emno>/',views.dbupdate,name='updateemployeeurl'),
    path('delete/<int:emno1>/',views.dbdelete,name='deleteemployeeurl'),
    path('detail/<int:eno>/',views.dbdetail,name='detailemployeeurl'),
    path('search/',views.dbsearch,name='searchemployeeurl')
    #path('updateemp/',views.dbupdate2,name='updateemployeeurl'),
]