from django.shortcuts import render
from core.models import Profile, About, ExperienceCategory, Project

def index(request):
    profile = Profile.objects.first()
    about = About.objects.first()
    experiences = ExperienceCategory.objects.prefetch_related("skills")
    projects = Project.objects.all()
    
    return render (request, 'index.html', {'profile': profile, 
                                           'about': about, 
                                           "experiences": experiences,
                                           "projects":projects})
