from django.urls import path

from user.views import signup

from user.views import login

from user.views import view_job_detail

from user.views import search_jobs

from user.views import job_apply

urlpatterns = [
    path('signup/',signup),
    path('login/',login),
    path('view_job_detail/',view_job_detail),
    # path('job_apply/',job_apply),
    path('jobs/<int:job_id>/apply/', job_apply, name='job_apply'),
    path('search_jobs/',search_jobs)
]