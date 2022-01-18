from django.db import close_old_connections
from django.db.models.query import QuerySet
from import_export import fields, resources
from .models import *
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from django.contrib.auth.models import User

class ManyToManyWidgetWithCreation(ManyToManyWidget):

    def __init__(self, model, field="pk", create=False, **kwargs):
        self.model = model
        self.field = field
        self.create = create
        super(ManyToManyWidgetWithCreation, self).__init__(model, field=field, **kwargs)

    def clean(self, value, **kwargs):

        if not value:
            return self.model.objects.none()

        cleaned_value: QuerySet = super(ManyToManyWidgetWithCreation, self).clean(
            value, **kwargs
        )
        object_list = value.split(self.separator)

        if len(cleaned_value.all()) == len(object_list):
            return cleaned_value

        if self.create:
            for object_value in object_list:
                _instance, _new = self.model.objects.get_or_create(
                    **{self.field: object_value}
                )

        model_objects = self.model.objects.filter(**{f"{self.field}__in": object_list})

        return model_objects

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email')

# class SkillsResource(resources.ModelResource):
#     # skill_type = fields.Field(
#     #             column_name='skill_type',
#     #             attribute="skill_type",
#     #             widget=ForeignKeyWidget(SkillType, 'type'))
#     skill_name=fields.Field(
#         column_name='skill_name',
#         attribute='skill_name',
#     )

#     class Meta:
#         model = Skills
#         fields=('id','skill_type','skill_name')

class ProjectsResource(resources.ModelResource):
    project_name=fields.Field(
        column_name='project_name',
        attribute='project_name',
    )
    frontend_tech = fields.Field(
                column_name='frontend_tech',
                attribute="frontend_tech",
                widget=ManyToManyWidgetWithCreation(FrontEndSkills, 'name'))
    backend_tech = fields.Field(
                column_name='backend_tech',
                attribute="backend_tech",
                widget=ManyToManyWidgetWithCreation(BackEndSkills, 'name'))
    devops_tech = fields.Field(
                column_name='devops_tech',
                attribute="devops_tech",
                widget=ManyToManyWidgetWithCreation(DevOpsSkills, 'name'))
    project_members = fields.Field(
                column_name='project_members',
                attribute="project_members",
                widget=ManyToManyWidgetWithCreation(Employee, 'employee'))
    product_manager = fields.Field(
                column_name='product_manager',
                attribute="product_manager",
                widget=ForeignKeyWidget(Employee, 'employee'))
    project_status=fields.Field(
        column_name='status',
        attribute='status',
    )
    def before_import_row(self, row, **kwargs):
        front_list=row.get('frontend_tech').split(',')  
        back_list=row.get('frontend_tech').split(',')  
        devops_list=row.get('frontend_tech').split(',')  
        members_list=row.get('project_memebers').split(',')
        for skill in front_list:
            FrontEndSkills.objects.get(name=skill)
        for skill in back_list:
            BackEndSkills.objects.get(name=skill)
        for skill in devops_list:
            DevOpsSkills.objects.get(name=skill)
        for name in members_list:
            Employee.objects.get(employee=name)

    class Meta:
        model = Projects
        fields=('id','project_name','frontend_tech','backend_tech','devops_tech','project_members','product_manager')

class EmployeeSkillResource(resources.ModelResource):
    employee = fields.Field(
                column_name='employee',
                attribute='employee',
                widget=ForeignKeyWidget(Employee, 'employee'))
    skill_type = fields.Field(
                column_name='skill_type',
                attribute='skill_type',
                widget=ManyToManyWidgetWithCreation(SkillType, 'type'))
    frontend_tech_stack = fields.Field(
                column_name='frontend_tech_stack',
                attribute='frontend_tech_stack',
                widget=ManyToManyWidgetWithCreation(FrontEndSkills, 'name'))
    backend_tech_stack = fields.Field(
                column_name='backend_tech_stack',
                attribute='backend_tech_stack',
                widget=ManyToManyWidgetWithCreation(BackEndSkills, 'name'))
    cloud_tech_stack = fields.Field(
                column_name='cloud_tech_stack',
                attribute='cloud_tech_stack',
                widget=ManyToManyWidgetWithCreation(CloudSkills, 'name'))
    database_tech_stack = fields.Field(
                column_name='database_tech_stack',
                attribute='database_tech_stack',
                widget=ManyToManyWidgetWithCreation(DatabaseSkills, 'name'))
    current_project = fields.Field(
                column_name='current_project',
                attribute='current_project',
                widget=ManyToManyWidgetWithCreation(Projects, 'project_name'))
    # current_project_skill = fields.Field(
    #             column_name='current_project_skill',
    #             attribute='current_project_skill',
    #             widget=ManyToManyWidgetWithCreation(Skills, 'skill_name'))
    status=fields.Field(
        column_name='status',
        attribute='status',
    )
    experience=fields.Field(
        column_name='experience',
        attribute='experience',
    )
    def before_import_row(self, row, **kwargs):
        frontend_list=row.get('frontend_tech_stack').split(',')
        backend_list=row.get('backend_tech_stack').split(',')
        database_list=row.get('database_tech_stack').split(',')
        cloud_list=row.get('cloud_tech_stack').split(',')
        skill_type_list=row.get('skill_type').split(',')
        # current_list=row.get('current_project_skill').split(',')
        # current_project_skills_list=row.get('skill_type').split(',')
        project_list=row.get('current_project').split(',')
        Employee.objects.get_or_create(
            employee=row.get('employee')
        )
        for type in skill_type_list:
            SkillType.objects.get(type=type)
        
        for skill in frontend_list:
            FrontEndSkills.objects.get(name=skill)
        for skill in backend_list:
            BackEndSkills.objects.get(name=skill)
        for skill in database_list:
            DatabaseSkills.objects.get(name=skill)
        for skill in cloud_list:
             CloudSkills.objects.get(name=skill)
        # for skill in current_list:
        #     Skills.objects.get(skill_name=skill)
        # for skill in current_project_skills_list:
        #     Skills.objects.get(skill_name=skill)
        for project in project_list:
            Projects.objects.get_or_create(
            project_name=project
        )
       
    class Meta:
        model=EmployeeSkills 
        skip_unchanged = False
        fields=('employee','id','project_name')
        
















 # type=SkillType.objects.get(type=row.get('skill_type'))
        # current_id = SkillType.objects.values_list('id', flat=True).filter(type = row.get('skill_type'))
        # print(current_id)
        # Skills.objects.get_or_create(id=current_id)
        # print(row.get('skill_type'))
        # print(type.id)



  # print(SkillType.objects.values_list('id',flat=True).get_or_create(
        #      type=row.get('skill_type')))
        # list=SkillType.objects.only('id').get(type=row.get('skill_type'))
        # print(list)
        # Skills.objects.get_or_create(
        #     skill_name=row.get('skills'),
        #     skill_type=row.get('skill_type'))
        # )
        # skill_name=row.get('skills'),
        #     skill_type_id= SkillType.objects.get(row.get('skill_type'))
        #     skill_type=row.get('skill_type')
        # print(SkillType.objects.all())



# class ForeignKeyWidgetWithCreation(ForeignKeyWidget):

#     def __init__(self, model, field="pk", create=False, **kwargs):
#         self.model = model
#         self.field = field
#         self.create = create
#         super(ForeignKeyWidgetWithCreation, self).__init__(model, field=field, **kwargs)

#     def clean(self, value, **kwargs):
#         if not value:
#             return None

#         if self.create:
#             self.model.objects.get_or_create(**{self.field: value})

#         val = super(ForeignKeyWidgetWithCreation, self).clean(value, **kwargs)

#         return self.model.objects.get(**{self.field: val}) if val else None

# class  AssetTrackerResources(resources.ModelResource):
#     class Meta:
#         model=AssetTracker
#         fields =("asset_type__asset_type","system_id","password","purchased_date","allocated_employee__allocated_employee","employee_email","brand","Processor","ram","disk","os","license","mac_address","allocation","comments")
#         export_order=("allocated_employee__allocated_employee","asset_type__asset_type","system_id","password","purchased_date","employee_email","brand","Processor","ram","disk","os","license","mac_address","allocation","comments")
