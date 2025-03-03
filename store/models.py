from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.
class HomePage(models.Model):
    HomePageSeasonTitle=models.CharField(max_length=200,blank=True,null=True)
    HomePageImage = models.ImageField()
    HomePageImageTitle = models.CharField(max_length=200,blank=True,null=True)
    HomePageParagraph = models.TextField(blank=True,null=True)

class WebSiteInfo(models.Model):
    Logo = models.ImageField(null=True,blank=True)
    Address=models.CharField(max_length=250,blank=True,null=True)
    PhoneNumber=models.CharField(max_length=250,blank=True,null=True)
    Email=models.CharField(max_length=250,blank=True,null=True)

    @property
    def imageURL(self):
        try:
            url = self.Logo.url
        except:
            url = ''
        return url

class Category(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    isNew = models.BooleanField(default=False,verbose_name="منتج جديد")
    isOnSale = models.BooleanField(default=False,verbose_name="المنتج عليه عرض")
    SalePrice = models.FloatField(default=0,blank=True,null=False,verbose_name="سعر العرض")
    isSoldOut = models.BooleanField(default=False,verbose_name="المنتج غير متاح")
    slug = models.SlugField(max_length=200,null=True,blank=True,allow_unicode=True)
    desc = models.TextField(blank=True,null=True)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    

import string
import random
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    print("RANDOM_STRING: ",''.join(random.choice(chars) for _ in range(size))) 
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        print("INSTANCE_NAME: ",instance.name)
        slug = slugify(instance.name,allow_unicode=True)#allow unicode in slugify function
    print("UNIQUE_SLUG: ",slug)
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists()
    if qs_exists:
        new_slug= "{slug}-{randString}".format(slug=slug,randString=random_string_generator())
        return unique_slug(instance,new_slug=new_slug)
    return slug

def pre_save_reciever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug(instance)

pre_save.connect(pre_save_reciever,sender=Product)