from django.contrib import admin

# Register your models here.
from . models import Department, Course, Details


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Department,DepartmentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','description','fees','seat_available']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['description','fees','seat_available']
    list_per_page = 20


admin.site.register(Course,CourseAdmin)
admin.site.register(Details)