from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    work = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to="profile/")
    cv = models.FileField(upload_to="cv/", null=True, blank=True)
    
    def __str__(self):
        return self.first_name
    
class About(models.Model):
    profile_picture = models.ImageField(upload_to="profile/")
    description = models.TextField()
    
class ExperienceCategory(models.Model):
    name = models.CharField(max_length=20)   
    
    def __str__(self):
        return self.name 
    
class Skill(models.Model):
    category = models.ForeignKey(ExperienceCategory, on_delete=models.PROTECT, default=1, related_name = "skills")
    name = models.CharField(max_length=20)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name