


from admin_portal.views import admin_login
from django.urls import path

from admin_portal.views import view_all_applicant,view_all_recruiter,delete_applicant

from admin_portal.views import view_rejected_recruiter

from admin_portal.views import delete_recruiter

from admin_portal.views import change_status,view_pending_recruiters

from admin_portal.views import view_active_recruiter

from admin_portal.views import rejected_change_status

from admin_portal.views import is_approval_job

urlpatterns = [
     path('admin_login/',admin_login),
    path('view_all_applicant/',view_all_applicant),
    path('delete_applicant/',delete_applicant),
    path('view_all_recruiter/',view_all_recruiter),
    path('view_pending_recruiters/',view_pending_recruiters),
    path('view_active_recruiter/',view_active_recruiter),
    path('view_rejected_recruiter/',view_rejected_recruiter),
    path('delete_recruiter/',delete_recruiter),
    path('change_status/',change_status),
    path('rejected_change_status/',rejected_change_status),
    path('is_approval_job/',is_approval_job)
 ]
