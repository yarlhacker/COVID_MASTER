from django.db import models


class Base(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract =  True


class Banner(Base):
   
    titre = models.CharField(max_length=255) 
    description = models.TextField() 
    image = models.FileField() 

    class Meta():
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.titre


class Protect(Base):
   
    image = models.FileField() 


    class Meta():
        verbose_name = 'Protect'
        verbose_name_plural = 'Protects'


class Optionprotect(Base):
   
    nom = models.CharField(max_length=255) 
    protect = models.ForeignKey('website.Protect', related_name='ProtectOption', on_delete=models.CASCADE)
  
    class Meta():
        verbose_name = 'Optionprotect'
        verbose_name_plural = 'Optionprotects'

    def __str__(self):
        return self.nom


class About(Base):
   
    titre = models.CharField(max_length=255) 
    description = models.TextField() 
    image = models.FileField() 
  
    class Meta():
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.titre


class Doctor(Base):
   
    titre = models.CharField(max_length=255) 
    description = models.TextField() 
    image = models.FileField() 
    lien = models.URLField(max_length=200)

  
    class Meta():
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.titre


class News(Base):
   
    titre = models.CharField(max_length=255) 
    description = models.TextField() 
    image = models.FileField() 
    

  
    class Meta():
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.titre




class Newsletter(Base):
   
    email = models.EmailField( max_length=254)
      
    class Meta():
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email



class Configuration(Base):

    entete_protect = models.CharField(max_length=255) 
    entete_news = models.CharField(max_length=255) 
    entete_newsletter = models.CharField(max_length=255)
    copyrights =  models.CharField(max_length=255)

    
      
    class Meta():
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'


class Website(Base):

    description_protect = models.TextField() 
    description_news = models.TextField() 
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    map =  models.CharField(max_length=255)

    
      
    class Meta():
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'







# Create your models here.
