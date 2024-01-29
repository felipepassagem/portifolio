from django.db import models



# Create your models here.
class Project(models.Model):
  projectName = models.CharField(max_length=80, blank=True, null=True)
  projectDescription = models.TextField(null=True, blank=True)
  projectCreatedAt = models.DateField(auto_now=False, blank=True, null=True)
  finalUser = models.CharField(max_length=80, blank=True, null=True)
  produtImg = models.ImageField(null=True, blank=True)
  

  def __str__(self):
    return self.projectName

class Me(models.Model):
  name = models.CharField(max_length=80, blank=True, null=True)
  cel = models.CharField(max_length=80, blank=True, null=True)
  email = models.CharField(max_length=80, blank=True, null=True)
  linkedin = models.CharField(max_length=80, blank=True, null=True)
  instagram = models.CharField(max_length=80, blank=True, null=True)
  github = models.CharField(max_length=80, blank=True, null=True)
  birthDate = models.DateField(auto_now=False, blank=True, null=True)
  description = models.CharField(max_length=2000, blank=True, null=True)
  obs = models.CharField(max_length=2000, blank=True, null=True)
  img = models.ImageField(null=True, blank=True)

  def __str__(self):
    return self.name

class Tec(models.Model):
  tecName = models.CharField(max_length=80, blank=True, null=True)
  tecLogo = models.ImageField(null=True, blank=True)
  tecText = models.CharField(max_length=500, blank=True, null=True)

  def __str__(self):
    return self.tecName

class Carousel(models.Model):
  carTitle = models.CharField(max_length=80, blank=True, null=True)
  carImg = models.ImageField(null=True, blank=True)
  carText = models.CharField(max_length=500, blank=True, null=True)
  carSubText = models.CharField(max_length=500, blank=True, null=True)
  

  def __str__(self):
    return self.carTitle
