from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=10,primary_key=True)
    
    def __str__(self):
        return self.emp_id

class Country(models.Model):
    
    country_name = models.CharField(max_length=10,primary_key=True)
    salary_slab = models.IntegerField()
    tax = models.FloatField()
    gov_leaves = models.IntegerField()
    
    def __str__(self):
        return self.country_name

class Region(models.Model):
    country_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    region_name = models.CharField(max_length=50)
    regional_leaves = models.IntegerField(default=5)
    
    def __str__(self):
        return self.region_name

class Employment(models.Model):
    emp_id = models.OneToOneField(Employee,on_delete=models.CASCADE)
    emp_typ = models.CharField(max_length=50)
    salary = models.FloatField()
    org_leaves = models.IntegerField()
    variables = models.FloatField()
    
   
