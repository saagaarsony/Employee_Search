from django.contrib import admin
from .models import Employee
from .models import Department

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "mobile", "department", "address", "dob", "doj"]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "deptname", "depttype", "deptblock"]
