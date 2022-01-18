from django.db import models
from crum import get_current_user
from django.core.validators import RegexValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from smart_selects.db_fields import ChainedManyToManyField,ChainedForeignKey
from smart_selects.db_fields import GroupedForeignKey
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils import Choices
# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modeified_date=models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True        

class AssetType(BaseModel):
    asset_type=models.CharField(max_length=50, blank=False)

    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_Asset_Type"
        verbose_name = "Asset Type"
        verbose_name_plural = "Asset Types"

    def __str__(self):
        return self.asset_type                             

class Employee(BaseModel):
    employee=models.CharField(max_length=50,blank=False,null=True,unique=True)
    designation= models.CharField(max_length=50, blank=True,
                        choices=[('Intern',' Intern'),
                                ('Software Engineer', 'Software Engineer'),
                                ('Senior Software Engineer','Senior Software Engineer'),
                                ('Business Associate','Business Associate'),
                                ('HR Associate','HR Associate'),
                                ('UI/UX Designer','UI/UX Designer'),
                                ('Associate Business Manager','Associate Business Manager'),
                                ('Senior HR Manager','Senior HR Manager'),
                                ('Product Manager','Product Manager')]) 

    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_employee"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.employee 

class AssetTracker(BaseModel):
    asset_type=models.ForeignKey(AssetType, on_delete=models.CASCADE, related_name='asset_types', blank=False)
    system_id=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=100,blank=True,null=True)
    purchased_date=models.DateField(blank=False)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE, related_name='employe', blank=False,null=True)
    employee_email=models.EmailField(max_length=254,blank=False)
    brand=models.CharField(max_length=100,blank=False)
    processor=models.CharField(max_length=100,blank=True, null=True)
    ram=models.CharField(max_length=100,blank=True, null=True)
    disk=models.CharField(max_length=100,blank=True, null=True)
    os=models.CharField(max_length=100,blank=True, null=True)
    license=models.CharField(max_length=50, blank=True, null=True, default='Valid',
                        choices=[('Valid', 'valid'),
                                ('Invalid', 'Invalid')])
    mac_address=models.CharField(max_length=100,blank=True, null=True)
    allocation=models.CharField(max_length=50, blank=False, default='Assigned',
                        choices=[('Assigned', 'Assigned'),
                                ('Unassigned', 'Unassigned'),
                                ('Service','Service')])
    comments=models.CharField(max_length=300,blank=True)
    system_image=models.ImageField(upload_to='system_image_uploades/', blank=False)

    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_Asset_Tracker"
        verbose_name = "Asset Tracker"
        verbose_name_plural = "Asset Trackers"

class GeneralImages(models.Model):
    general_image=models.ImageField(upload_to='general_image_uploades/', blank=False)

    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_General_Images"
        verbose_name = "General Image"
        verbose_name_plural = "General Images"

class SkillType(BaseModel):
    type=models.CharField(max_length=100,blank=False,unique=True)
    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_skill_type"
        verbose_name = "Skill Type"
        verbose_name_plural = "Skill Types"
    def __str__(self):
        return self.type

class FrontEndSkills(BaseModel):
    name=models.CharField(max_length=100,blank=False,unique=True,null=False)
    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_frontendskills"
        verbose_name = "FrontEndSkills"
        verbose_name_plural = "FrontEndSkillss"
    def __str__(self):
        return self.name 

class BackEndSkills(BaseModel):
    name=models.CharField(max_length=100,blank=False,unique=True,null=False)
    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_backendskills"
        verbose_name = "BackEndSkills"
        verbose_name_plural = "BackEndSkillss"
    def __str__(self):
        return self.name 
class DatabaseSkills(BaseModel):
    name=models.CharField(max_length=100,blank=False,unique=True,null=False)
    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_databaseskills"
        verbose_name = "DatabaseSkills"
        verbose_name_plural = "DatabaseSkillss"
    def __str__(self):
        return self.name 
class CloudSkills(BaseModel):
    name=models.CharField(max_length=100,blank=False,unique=True,null=False)
    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_cloudskills"
        verbose_name = "CloudSkills"
        verbose_name_plural = "CloudSkillss"
    def __str__(self):
        return self.name 
class DevOpsSkills(BaseModel):
    name=models.CharField(max_length=100,blank=False,unique=True,null=False)
    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_devopsskills"
        verbose_name = "DevOpsSkills"
        verbose_name_plural = "DevOpsSkillss"
    def __str__(self):
        return self.name 


class Projects(BaseModel):
    project_name=models.CharField(max_length=100,blank=False,unique=True)
    frontend_tech=models.ManyToManyField(FrontEndSkills,related_name='project_frontend_skill')
    backend_tech=models.ManyToManyField(BackEndSkills,related_name='project_backend_skill')
    devops_tech=models.ManyToManyField(DevOpsSkills,related_name='project_devops_skill')
    project_members=models.ManyToManyField(Employee,related_name='project_project_members')
    product_manager=models.ForeignKey(Employee,on_delete=CASCADE,related_name='project_product_manager',blank=False,null=True)
    project_status = models.CharField(max_length=50, blank=True,
                        choices=[('New', 'New'),
                                ('Open', 'Available'),
                                ('In Progress','In Progress'),
                                ('Completed','Completed')]) 
    class Meta:
        managed = True
        app_label = 'asset_tracker'
        db_table = "asset_tracker_project"
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.project_name 

class EmployeeSkills(BaseModel):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_details_skills', blank=False,null=True)
    experience = models.CharField(max_length=100,blank=True,null=True)
    skill_type = models.ManyToManyField(SkillType, related_name='employee_skill_type', blank=False)
    frontend_tech_stack = models.ManyToManyField(FrontEndSkills,related_name='employee_frontend_skills',blank=True)
    backend_tech_stack = models.ManyToManyField(BackEndSkills, related_name='employee_backend_skills',blank=True)
    database_tech_stack = models.ManyToManyField(DatabaseSkills,related_name='employee_database_skills',blank=True)
    cloud_tech_stack = models.ManyToManyField(CloudSkills,related_name='employee_cloud_skills',blank=True)
    current_project = models.ManyToManyField(Projects, related_name='employee_projects', blank=True)
    # current_project_skill=models.ManyToManyField(Skills, related_name='employee_current_skill', blank=False)
    status = models.CharField(max_length=50, blank=True,
                        choices=[('Occupied', 'Occupied'),
                                ('Available', 'Available')]) 
    class Meta:
        app_label = 'asset_tracker'
        db_table = "asset_tracker_employee_skills"
        verbose_name = "Employee Skills"
        verbose_name_plural = "Employee Skills"
        verbose_name_plural = "Employee Skills"  





















