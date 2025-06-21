from django.urls import path
from . import views
urlpatterns=[
    # Function Based Views
    path('students/',views.studentsViews),
    path('students/<int:pk>/',views.studentsdataview),

    # Classed Based Views 
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>',views.EmployeeDetail.as_view())
    # tell this url pattern to treat as Class based VIew 
]