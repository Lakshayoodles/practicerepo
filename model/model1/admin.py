from django.contrib import admin
from .models import studentlist # Import your model

@admin.register(studentlist)
class StudentlistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'classs', 'phone_number', 'guardian_name') # Fields to show in list view
    search_fields = ('first_name', 'last_name', 'address', 'guardian_name') # Enable search
    list_filter = ('classs',) # Enable filtering by class