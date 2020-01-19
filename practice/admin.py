from django.contrib import admin

from .models import Track, Subdomain, Question, TestCases
# Register your models here.

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class SubdomainInline(admin.StackedInline):
    model = Subdomain

class SubdomainAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Track',              {'fields': ['track']}),
        ('Name',               {'fields': ['name']}),
    ]
    inlines = [QuestionInline]

    list_display = ('name', 'track')

class TrackAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
    ]
    inlines = [SubdomainInline]

admin.site.register(Subdomain, SubdomainAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Question)
admin.site.register(TestCases)
