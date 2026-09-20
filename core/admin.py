from django.contrib import admin
from core.models import Profile, About, ExperienceCategory, Skill, Project

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "work", "profile_picture", "cv"]
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["profile_picture", "description"]
   
@admin.register(ExperienceCategory)
class ExperienceCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]  
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [ "name","category", "description"]
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["image", "name","description", "github", "pdf"]