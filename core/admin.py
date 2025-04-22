from django.contrib import admin
from .models import AboutInfo, Hero, StatItem, Skill

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
