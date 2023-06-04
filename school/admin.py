from django.contrib import admin

from .models import Students, Teachers


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    pass
