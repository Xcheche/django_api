from django.contrib import admin
from courses.models import Course
# Register your models here.



class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Names of Courses", {"fields": ["name"]}),
        ("Programming Languages", {"fields": ["language"]}),
        ("Prices", {"fields": ["price"]}),
    ]




admin.site.register(Course, CourseAdmin)