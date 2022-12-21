from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio,Experience


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]

#Experience
class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
     inlines = []


# Portfolio
admin.site.register(Portfolio)