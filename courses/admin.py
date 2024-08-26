from django.contrib import admin
from courses.models import Course
# Register your models here.



class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Names of Courses", {"fields": ["name"]}),
        ("Programming Languages", {"fields": ["language"]}),
        ("Prices", {"fields": ["price"]}),
    ]
    list_display = ("name", "language", "price")
    search_fields = ("name", "language", "price")
    list_filter = ("language",)
    list_per_page = 1
    # prepopulated_fields = {"language": ("name",)}
    # ordering = ("name",)
    def get_ordering(self, request):
        if request.user.is_superuser:
            # Superusers see the ordering as defined by the model
            return ['name']  # Replace 'field_name' with the field you want to order by
        else:
            # Non-superusers see the default ordering
            return super().get_ordering(request)




admin.site.register(Course, CourseAdmin)