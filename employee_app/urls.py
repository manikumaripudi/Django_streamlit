"""
URL configuration for employee_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# employee_app/urls.py

from django.urls import path
from .views import EmployeeCreate, EmployeeRetrieve, EmployeeUpdate, EmployeeDestroy, EmployeeList

urlpatterns = [
    path('create/', EmployeeCreate.as_view(), name='employee-create'),
    path('<int:pk>/', EmployeeRetrieve.as_view(), name='employee-retrieve'),
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name='employee-update'),
    path('<int:pk>/delete/', EmployeeDestroy.as_view(), name='employee-destroy'),
    path('', EmployeeList.as_view(), name='employee-list'),
]

# from django.urls import path
# from .views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView

# urlpatterns = [
#     path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
#     path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
# ]
