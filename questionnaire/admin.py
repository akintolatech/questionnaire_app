from django.contrib import admin
from .models import Teacher, Question, Response, QuestionCategory

admin.site.register(Teacher)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(QuestionCategory)