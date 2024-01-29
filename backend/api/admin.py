from django.contrib import admin
from .models import Project, Me, Tec, Carousel

# Register your models here.
@admin.register(Project)
class Project(admin.ModelAdmin):
  list_display = ('projectName',)
  list_filter = ('projectName',)

  def __str__(self):
    return self.projectName

@admin.register(Me)
class Me(admin.ModelAdmin):
  list_display = ('name',)
  list_filter = ('name',)

  def __str__(self):
    return self.name

@admin.register(Tec)
class Tec(admin.ModelAdmin):
  list_display = ('tecName',)
  list_filter = ('tecName',)

  def __str__(self):
    return self.name

@admin.register(Carousel)
class Carousel(admin.ModelAdmin):
  list_display = ('carTitle',)
  list_filter = ('carTitle',)

  def __str__(self):
    return self.carTitle