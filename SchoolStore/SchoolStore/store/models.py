from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.


class Department(models.Model):

    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=300,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='department',blank=True)

    class Meta:
        ordering= ('name',)
        verbose_name='Department'
        verbose_name_plural='Departments'

    def get_url(self):
        return reverse('store:course_by_department',args=[self.slug])

    def __str__(self):
        return'{}'.format(self.name)


class Course(models.Model):

    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    fees=models.DecimalField(max_digits=10,decimal_places=2)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='course',blank=True)
    seat_available=models.BooleanField(default=True)
    # created=models.DateTimeField(auto_now_add=True)
    # updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='Course'
        verbose_name_plural='Courses'

    def get_url(self):
        return reverse('store:course_by_department',args=[self.department.slug, self.slug])



    def __str__(self):
        return '{}'.format(self.name)


class Details(models.Model):
    name = models.CharField(max_length=250)
    dob =  models.CharField(max_length=250)
    age =  models.CharField(max_length=5)
    gender = models.CharField(max_length=250)
    phn = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    address = models.TextField(blank=True)
    department = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    materials = models.TextField(blank=True)

    class Meta:
        db_table = 'Details'

    def __str__(self):
        return '{}'.format(self.name)