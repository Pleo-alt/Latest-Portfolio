from django.shortcuts import render
from core.models import Profile, About, ExperienceCategory

def index(request):
    profile = Profile.objects.first()
    about = About.objects.first()
    experiences = ExperienceCategory.objects.prefetch_related("skills")
    return render (request, 'index.html', {'profile': profile, 'about': about, "experiences": experiences})
