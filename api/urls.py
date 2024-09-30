from django.urls import path
from.import views

urlpatterns = [
    path('getemployee/',views.getemployeeapi),
    path('modify/<int:pk>/',views.modifyemployeeapi)
]