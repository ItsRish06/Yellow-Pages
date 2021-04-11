from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete,pre_save
from django.utils.text import slugify

class State(models.Model):
    name = models.CharField(max_length=50,unique=True,primary_key=True)

    def __str__(self):
        return self.name



class Religion(models.Model):
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




#NGO Model

class NGO(models.Model):
    title = models.CharField(max_length=150 , unique = True)
    state = models.ForeignKey(State,on_delete=models.DO_NOTHING,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,blank=True,null=True)
    religion = models.ForeignKey(Religion,on_delete=models.DO_NOTHING,blank=True,null=True)
    gender = models.ManyToManyField(Gender)
    stype = models.ForeignKey(Type,on_delete=models.DO_NOTHING,blank=True,null=True)
    eligibility = models.TextField(max_length=50000,blank=True,null=True)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING,blank=True,null=True)
    content = models.TextField(max_length = 50000,blank=True,null=True)
    updated_on = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=150,blank=True)
    site_url = models.CharField(max_length=300,null=True,blank=True)
    contact = models.CharField(max_length=150,null=True,blank=True)
    email = models.CharField(max_length=150,null=True,blank=True)
    location = models.TextField(max_length = 50000,blank=True,null=True)

    def __str__(self):
        return self.title


#creates slug from title before saving the object
def pre_save_bookbank_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_bookbank_receiver,sender=NGO)

