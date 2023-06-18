from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from app.forms import *
from django.db.models import Q
def home(request):
    return render(request,'home.html')

def create(request):
    
    d={'data':Employee_Form()}
    if request.method=='POST':
        empobj=Employee_Form(request.POST)
        if empobj.is_valid():
            emp_id=empobj.cleaned_data['emp_id']
            
            new_emp=Employee.objects.create(emp_id=emp_id)
            new_emp.save()

         
        d1={'data':Employment_Form()}
        if request.method=='POST':
            empmt_obj=Employment_Form(request.POST)
            if empmt_obj.is_valid():

                #emp_id=Employee.objects.earliest('emp_id')
                emp_id=empmt_obj.cleaned_data['emp_id']
                emp_typ=empmt_obj.cleaned_data['emp_typ']
                salary=empmt_obj.cleaned_data['salary']
                org_leaves=empmt_obj.cleaned_data['org_leaves']
                variables=0.1*salary
                new_empmt=Employment.objects.create(emp_id=emp_id,emp_typ=emp_typ,salary=salary,org_leaves=org_leaves,variables=variables)
                new_empmt.save()
                return render(request,'create.html',d)
        return render(request,'create.html',d1)
            

    return render(request,'create.html',d)

def calculator(request):
    d={'data':Calculation_Form()}
    if request.method=='POST':
        selectobj=Calculation_Form(request.POST)
        if selectobj.is_valid():
            emp=selectobj.cleaned_data['select_emp_id']
            country=selectobj.cleaned_data['select_country']
            region=selectobj.cleaned_data['select_region']
            gov_leaves=Country.objects.get(country_name=country).gov_leaves
            org_leaves=Employment.objects.get(emp_id=emp).org_leaves
            reg_leaves=Region.objects.get(Q(country_name=country) & Q(region_name=region)).regional_leaves
            total_leaves=org_leaves + gov_leaves + reg_leaves
            #print(org_leaves,gov_leaves,reg_leaves,total_leaves)
            salary=Employment.objects.get(emp_id=emp).salary
            variables=Employment.objects.get(emp_id=emp).variables
            emp_type=Employment.objects.get(emp_id=emp).emp_typ
            slab=Country.objects.get(country_name=country).salary_slab
            if country=='INDIA':
                if salary<700000:
                    tax_amount=0
                elif salary>700000 and salary<1000000:
                    tax_amount=0.1 * salary
            else:
                tax_amount=Country.objects.get(country_name=country).tax * salary
            net_pay=salary + variables - slab - tax_amount
            d={'gl':gov_leaves,'rl':reg_leaves,'ol':org_leaves,'tl':total_leaves,'sl':salary,'vr':variables,'sb':slab,'tx':tax_amount,'np':net_pay,'emp':emp,'ct':country,'rg':region,'et':emp_type}
            return render(request,'report.html',d)
    return render(request,'calculator.html',d)