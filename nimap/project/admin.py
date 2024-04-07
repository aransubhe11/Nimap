from django.contrib import admin
from django.contrib import admin
from .models import User ,Clients,Project

@admin.register(Clients)
class Clientadmin(admin.ModelAdmin):
    list_display=('id','client_name','created_at','created_by','updated_at')
    
    
@admin.register(Project)
class Projectadmin(admin.ModelAdmin):
    list_display=('id','projects','project_name','created_by','created_at')
    
    