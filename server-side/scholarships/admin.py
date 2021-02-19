from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ScholarshipAdmin(SummernoteModelAdmin,):
    list_display = ('title','updated_on','deadline')
    search_fields=('title',)
    list_filter = ('sclass','course','updated_on','gender','stype','country','state','religion')
    summernote_fields = '__all__' 
 

admin.site.register(State)
admin.site.register(Country)
admin.site.register(Course)
admin.site.register(Religion)
admin.site.register(Gender)
admin.site.register(Class)
admin.site.register(Scholarship,ScholarshipAdmin)
