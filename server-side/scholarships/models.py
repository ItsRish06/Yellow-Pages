from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete,pre_save
from django.utils.text import slugify

class State(models.Model):
    name = models.CharField(max_length=50,unique=True,primary_key=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50,unique=True,primary_key=True)
    
    def __str__(self):
        return self.name

class Religion(models.Model):
    name = models.CharField(max_length=50,unique=True,primary_key=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50,unique=True,primary_key=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=150,unique=True,primary_key=True)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=150,unique=True,primary_key=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=150,unique=True,primary_key=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150,unique=True,primary_key=True)

    def __str__(self):
        return self.name


""" TYPE = (
    ('Government','Government'),
    ('Private','Private'),
    ('International','International')
)

COUNTRY_CHOICES = (
        ('India','India'),
        ('Study Abroad','Study Abroad')
)

ELIGIBILITY_CHOICES = (
        ('Merit','Merit Based'),
        ('Income Based','Income Based'),
        ('Sports Talent','Educational Qualification'),
        ('Other','Other'),
        
)

CATEGORY_CHOICES = (
    ('SC/ST/OBC','SC/ST/OBC'),
    ('Minority','Minority'),
    ('Physically Disabled','Physically Disabled'),
    ('Others' , 'Others')
) """

def upload_location(instance,filename):
    file_path = 'scholarships/logo/{title}_{filename}'.format(
        title = str(instance.title),filename=filename
    )
    return file_path


#Scholarship Model

class Scholarship(models.Model):
    title = models.CharField(max_length=150 , unique = True)
    about = models.TextField(max_length = 5000 , blank=True,null=True )
    image = models.ImageField(upload_to=upload_location,null=True,blank=True)
    state = models.ForeignKey(State,on_delete=models.DO_NOTHING,blank=True,null=True)
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,blank=True,null=True)
    religion = models.ForeignKey(Religion,on_delete=models.DO_NOTHING,blank=True,null=True)
    sclass = models.ManyToManyField(Class)
    gender = models.ManyToManyField(Gender)
    stype = models.ForeignKey(Type,on_delete=models.DO_NOTHING,blank=True,null=True)
    eligibility = models.TextField(max_length=50000,blank=True,null=True)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING,blank=True,null=True)
    content = models.TextField(max_length = 50000,blank=True,null=True)
    award = models.CharField(max_length=150)
    updated_on = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=150,blank=True)
    site_url = models.CharField(max_length=300,null=True,blank=True)
    deadline = models.DateField(auto_now_add=False,auto_now=False)
    contact = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.title

@receiver(post_delete,sender=Scholarship)
def submission_delete(sender,instance,*args,**kwargs):
    instance.image.delete(False)

#creates slug from title before saving the object
def pre_save_scholarship_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_scholarship_receiver,sender=Scholarship)

