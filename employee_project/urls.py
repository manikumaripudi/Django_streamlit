#employee_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employee_app.urls')),
]
# from django.contrib import admin
# from django.urls import path, include
# from employee_app.views import employee_management_view  # Import the view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('employee_app.urls')),
#     path('', employee_management_view, name='employee-management'),  # Add this line
# ]
