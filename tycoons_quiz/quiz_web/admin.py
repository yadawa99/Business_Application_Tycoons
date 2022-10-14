from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Quiz)

class AnswerInLine(admin.TabularInline):
    model = Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Marks_Of_User)