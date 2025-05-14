from django.contrib import admin
from django.db import models
from .models import AboutInfo, Hero, StatItem, Skill, WorkExperience

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('heading',)

@admin.register(StatItem)
class StatItemAdmin(admin.ModelAdmin):
    list_display = ('large_text', 'small_text')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_level_display')
    list_filter = ('level',)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'start', 'end', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    fields = (
        'order', 'start', 'end', 'title', 'organization',
        'description', 'projects', 'tech_stack'
    )
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows':2, 'cols':40})},
    }