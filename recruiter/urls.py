
from django.urls import path
from recruiter.views import signup
from recruiter.views import login
from recruiter.views import create_job
from recruiter.views import job_list
from recruiter.views import delete_job
from recruiter.views import update_job
from recruiter.views import view_all_applicant

urlpatterns = [
  path('signup/',signup),
  path('login/',login),
  path('create_job/',create_job),
  path('job_list/',job_list),
  path('delete/',delete_job),
   # path('update_job/',update_job),
   path('jobs/update/<int:id>/', update_job, name='update_job'),
    path('view_all_applicant/',view_all_applicant),

 ]