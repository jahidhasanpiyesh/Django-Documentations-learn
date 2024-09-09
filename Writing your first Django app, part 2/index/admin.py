from django.contrib import admin

# Register your models here.
from .models import Question,Choice

@admin.register(Question)
class question(admin.ModelAdmin):
    list_display=['qustions_text']

    
admin.site.register(Choice)