from django.contrib import admin
from .models import UserProfile, UserRole, Privileges, Roles

class BaseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.username
        obj.updated_by = request.user.username
        super().save_model(request, obj, form, change)

class UserProfileAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.username
        obj.updated_by = request.user.username
        super().save_model(request, obj, form, change)

class UserRoleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.username
        obj.updated_by = request.user.username
        super().save_model(request, obj, form, change)

class PrivilegesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.username
        obj.updated_by = request.user.username
        super().save_model(request, obj, form, change)

class RolesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.username
        obj.updated_by = request.user.username
        super().save_model(request, obj, form, change)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Privileges, PrivilegesAdmin)
admin.site.register(Roles, RolesAdmin)
