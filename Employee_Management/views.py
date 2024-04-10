from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Employee_Management

# Create your views here.
def emp_home(request):

    emps=Employee_Management.objects.all()
    return render(request,"emp/home.html",{
        'emps':emps
    })

    # return render(request,"emp/home.html",{})

def add_emp(request):
    if request.method=='POST':
        print("Data is coming!!")

        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        #create model object and set the data
        emp=Employee_Management()
        emp.name=emp_name
        emp.emo_id=emp_id
        emp.phone=emp_phone
        emp.address=emp_address
        emp.working=emp_working
        emp.department=emp_department
        
        if emp_working is None:
            emp.working=False
        else:
            emp.working=True
        #save the object 
        emp.save()
        #prepare msg

        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    print(emp_id)
    emp=Employee_Management.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def edit_emp(request,emp_id):
    print(emp_id)
    emp=Employee_Management.objects.get(pk=emp_id)
    return render(request,"emp/edit_emp.html",{
        'emp':emp
    })

def do_edit_emp(request,emp_id):
    if request.method=='POST':
        # fetching all data from url
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        # Now update database
        emp=Employee_Management.objects.get(pk=emp_id)
        emp.name=emp_name
        emp.emo_id=emp_id_temp
        emp.phone=emp_phone
        emp.address=emp_address
        emp.working=emp_working
        emp.department=emp_department
        
        if emp_working is None:
            emp.working=False
        else:
            emp.working=True
        emp.save()
        # return redirect("/emp/home/")
    return redirect("/emp/home/")