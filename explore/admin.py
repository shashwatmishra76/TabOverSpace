from django.contrib import admin

from .models import Subtopic, Article
# Register your models here.

class ArticleInline(admin.StackedInline):
    model = Article
    extra = 10

class SubtopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
    ]
    inlines = [ArticleInline]

admin.site.register(Subtopic, SubtopicAdmin)
