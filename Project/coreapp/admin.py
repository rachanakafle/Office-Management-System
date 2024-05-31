
from django.contrib import admin

 # Register your models here.
from coreapp.models import MyUser, Partner, Developer, ProjectManager, Project

#
# class MyUserAdmin(admin.ModelAdmin):
#     list_display = ['first_name','last_name','email','is_active']# group
#
#
# class PartnerAdmin(admin.ModelAdmin):
#     list_display = ['partner_name','user', 'detail', 'project_file']
#     search_fields = ['user']
#
#
# class UserDetailAdmin(admin.ModelAdmin):
#     list_display = ['user', 'photo', 'contact', 'location', 'position', 'work', 'cv']
#
#
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['partner', 'project_name','theme']
#
#
# class ProjectDetailAdmin(admin.ModelAdmin):
#     list_display = ['project', 'CHOICES', 'status', 'start_date', 'end_date']
#
# class ProjectManagerAdmin(admin.ModelAdmin):
#     list_display = ['user_detail', 'project_detail']
#
# class DeveloperAdmin(admin.ModelAdmin):
#     list_display = ['user_detail', 'project_detail']


admin.site.register(MyUser)
admin.site.register(Partner)
admin.site.register(Project)
admin.site.register(ProjectManager)
admin.site.register(Developer)
