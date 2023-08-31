from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField( max_length=20,null=False)
    location=models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" %(self.name+",", self.location)

class Role(models.Model):
    name = models.CharField(max_length=35,null=False)
    def __str__(self):
        return  (self.name)

class Employee(models.Model):
    first_name = models.CharField( max_length=100, null=False)
    last_name = models.CharField( max_length=35, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField( max_length=15)  # Adjust max_length as needed
    hire_date = models.DateField()
    def __str__(self):
        return "%s %s , %s - %s - %s - %s - %s - %s" % (self.first_name, self.last_name, self.department.name, self.salary, self.bonus, self.role.name, self.phone, self.hire_date)
