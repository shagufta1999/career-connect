from django.contrib import admin

from recruiter.models import recruiter_info

from recruiter.models import Job

# Register your models here.
admin.site.register(recruiter_info)
admin.site.register(Job)