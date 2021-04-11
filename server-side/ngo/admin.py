from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class NGOAdmin(SummernoteModelAdmin,):
    list_display = ('title','updated_on',)
    search_fields=('title',)
    list_filter = ('updated_on','gender','stype','country','state','religion')
    summernote_fields = '__all__' 
 
class GenAdmin(SummernoteModelAdmin) :
    list_display = ('name',)

admin.site.register(State,GenAdmin)
admin.site.register(Country,GenAdmin)
admin.site.register(Religion,GenAdmin)
admin.site.register(Gender,GenAdmin)
admin.site.register(Category,GenAdmin)
admin.site.register(Type,GenAdmin)
admin.site.register(NGO,NGOAdmin)
