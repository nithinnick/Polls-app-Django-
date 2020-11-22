from django.contrib import admin

from .models import Question, Choice
# Register your models here.

admin.site.site_header = "Vote Polling"
admin.site.site_title = "Polling Admin"
admin.site.index_title = "Voting App"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields':['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)


