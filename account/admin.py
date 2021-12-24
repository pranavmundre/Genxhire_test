from django.contrib import admin
from account.models import Person, Employee


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')
    readonly_fields = ('modified_date', 'created_date')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('person', 'department', 'role', 'line_manager', 'created_date')


admin.site.register(Person, PersonAdmin)
admin.site.register(Employee, EmployeeAdmin)

