from django.shortcuts import render, redirect
from.models import Employee
from.models import Department
from django.contrib import messages
from django.db.models import Q 
from django.http import JsonResponse


def index(request):
    employees = Employee.objects.all()
    e_department = Department.objects.all()
    query = ""
    emp_name = ""
    emp_mobile = ""
    emp_email = ""
    emp_department = ""

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            department = request.POST.get("department")
            address = request.POST.get("address")
            dob = request.POST.get("dob")
            doj = request.POST.get("doj")
            Employee.objects.create(
                name=name,
                email=email,
                mobile=mobile,
                department=department,
                address=address,
                dob=dob,
                doj=doj
            )
            messages.success(request, "Employee Added successfully")
            return redirect("index")

        if "dept" in request.POST:
            deptname = request.POST.get("deptname")
            depttype = request.POST.get("depttype")
            deptblock = request.POST.get("deptblock") 
            Department.objects.create(
                deptname=deptname,
                depttype=depttype,
                deptblock=deptblock
            )  
            messages.success(request, "Department Added Successfully")
            return redirect("index")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            department = request.POST.get("department")
            address = request.POST.get("address")
            dob = request.POST.get("dob")
            doj = request.POST.get("doj")

            update_employee = Employee.objects.get(id=id)
            update_employee.name = name
            update_employee.email=email
            update_employee.mobile=mobile
            update_employee.department=department
            update_employee.address=address
            update_employee.dob=dob
            update_employee.doj=doj
            update_employee.save()

            messages.success(request, "Employee Updated Successfully")
            return redirect("index")

        elif "delete" in request.POST:
            id=request.POST.get("id")
            Employee.objects.get(id=id).delete()
            messages.success(request, "Employee Deleted Successfully")
            return redirect("index") 

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            employees = Employee.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(mobile__icontains=query) | Q(department__icontains=query))

        elif "searche" in request.POST:
          emp_name = request.POST.get("emp_name")
          emp_mobile = request.POST.get("emp_mobile")
          emp_email = request.POST.get("emp_email")
          emp_department = request.POST.get("emp_department")
    
          employees = Employee.objects.all() 
    
        if emp_name:
          employees = employees.filter(name__icontains=emp_name)
    
        if emp_mobile:
           employees = employees.filter(mobile__icontains=emp_mobile)

        if emp_email:
            employees = employees.filter(email__icontains=emp_email)

        if emp_department:   
            employees = employees.filter(department__icontains=emp_department) 

    context = {"employees": employees, "e_department": e_department, "query": query, "emp_name": emp_name, "emp_mobile": emp_mobile, "emp_email": emp_email, "emp_department": emp_department}
    return render(request, "index.html", context=context)
