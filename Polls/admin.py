from django.contrib import admin
from .models import Questions, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['published_on'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'published_on', 'was_published_recently')
    list_filter = ['published_on']
    search_fields = ['question_text']


admin.site.register(Questions, QuestionAdmin)

