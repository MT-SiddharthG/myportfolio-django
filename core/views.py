
from django.views.generic import TemplateView
from .models import Hero, AboutInfo, Skill, StatItem, WorkExperience

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['hero'] = Hero.objects.first()
        ctx['about'] = AboutInfo.objects.first()
        ctx['stats'] = StatItem.objects.all()
        ctx['skills'] = Skill.objects.all()
        return ctx



class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutInfo.objects.first()
        context['stats'] = StatItem.objects.all()
        context['skills'] = Skill.objects.all()
        return context
    

class ProjectsView(TemplateView):
    template_name = 'core/projects.html'
    # def get_context_data(self, **ctx):
    #     ctx = super().get_context_data(**ctx)
    #     ctx['projects'] = Project.objects.all()
    #     return ctx

class ExperienceView(TemplateView):
    template_name = 'core/experience.html'
    def get_context_data(self, **ctx):
        ctx = super().get_context_data(**ctx)
        ctx['jobs'] = WorkExperience.objects.all()
        return ctx

class ContactView(TemplateView):
    template_name = 'core/contact.html'