from django.contrib import admin

from .models import Module, Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk','question_text', 'module']
    ordering = ['module']
    #aqui se puede implementar la busqueda
#admin.site.register(Question, QuestionAdmin)

class QuestionInline(admin.StackedInline):
    model = Question
    

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_questions']
    inlines = [QuestionInline]
# Register your models here.

#admin.site.register(Module)
