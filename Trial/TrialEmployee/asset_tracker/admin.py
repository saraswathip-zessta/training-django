from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportMixin
from .resources import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
    
)
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class UserAdmin(ImportExportModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email')
    resource_class = UserResource
    pass

class AssetTrackerAdmin(ExportMixin,admin.ModelAdmin):
    # resource_class=AssetTrackerResources
    list_display = ( 'employee',)

class EmployeeSkillAdmin(ImportExportModelAdmin):
    list_display = ('employee', 'experience','status')
    search_fields = ("person_lastname__startswith", )
    list_display = ('employee', 'experience','status','project_working','frontend_list','backend_list','cloud_list','database_list')
    list_filter =('skill_type','status','current_project','frontend_tech_stack','database_tech_stack','backend_tech_stack','cloud_tech_stack','current_project',)
    search_fields = ("employee__employee", )
    # filter_horizontal = ('frontend_tech_stack',)
    resource_class = EmployeeSkillResource
    def frontend_list(self, obj):
        return "\n".join([s.name+"," for s in obj.frontend_tech_stack.all()])
    def backend_list(self, obj):
        return "\n".join([s.name+"," for s in obj.backend_tech_stack.all()])
    def cloud_list(self, obj):
        return "\n".join([s.name+"," for s in obj.cloud_tech_stack.all()])
    def devops_list(self, obj):
        return "\n".join([s.name+"," for s in obj.devops_tech_stack.all()])
    def database_list(self, obj):
        return "\n".join([s.name+"," for s in obj.database_tech_stack.all()])
    def project_working(self, obj):
        return "\n".join([s.project_name+"," for s in obj.current_project.all()])

# class SkillsAdmin(ImportExportModelAdmin):
#     # list_display = ('skill_name')
#     # list_filter =('skill_type',)
#     resource_class = SkillsResource

class ProjectsAdmin(admin.ModelAdmin):
    list_display=('project_name','product_manager','frontend','backend','devops','members','project_status')
    resource_class = ProjectsResource
    def frontend(self, obj):
        return "\n".join([s.name+"," for s in obj.frontend_tech.all()])
    def backend(self, obj):
        return "\n".join([s.name+"," for s in obj.backend_tech.all()])
    def devops(self, obj):
        return "\n".join([s.name+"," for s in obj.devops_tech.all()])
    def members(self, obj):
        return "\n".join([s.employee+"," for s in obj.project_members.all()])

class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ( 'asset_type',)

class AllocatedEmployeeAdmin(admin.ModelAdmin):
    list_display = ( 'employee',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(AssetTracker,AssetTrackerAdmin) 
admin.site.register(AssetType,AssetTypeAdmin)
admin.site.register(Employee,AllocatedEmployeeAdmin)
admin.site.register(EmployeeSkills,EmployeeSkillAdmin)
admin.site.register(FrontEndSkills)
admin.site.register(BackEndSkills)
admin.site.register(CloudSkills)
admin.site.register(DevOpsSkills)
admin.site.register(DatabaseSkills)
admin.site.register(SkillType)
admin.site.register(Projects,ProjectsAdmin)
    
# admin.site.register(Projects,ProjectsAdmin)
admin.site.register(GeneralImages) 