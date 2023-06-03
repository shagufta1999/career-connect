import datetime

from django.http import HttpResponse
import mysql.connector
from django.utils import timezone

from recruiter.models import Job

from user.models import JobApplicationform

from user.models import Applicant_info


# from django.shortcuts import render

# from recruiter.models import Job


def signup(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_psw=request.POST.get('confirm_psw')
        active_status=request.POST.get('active_status')

        if len(password)<8:
            return HttpResponse("please enter minimum 8 digit password")


        if password != confirm_psw:
            return HttpResponse('password do not match')

        dbconnect=mysql.connector.connect(
            host='localhost',
            user='root',
            password='Root@#$1234',
            database='codeplanet'
        )

        crs=dbconnect.cursor()

        query="select * from user_applicant_info where email= '"+email+"'"

        crs.execute(query)

        data=crs.fetchone()

        if data is None:
            query = "insert into user_applicant_info values('"+id+"','"+username+"','"+email+"','"+password+"','"+confirm_psw+"','"+active_status+"')"

            crs.execute(query)

            dbconnect.commit()
            return HttpResponse("registration successfully completed")
        else:
            return HttpResponse("you are already registered")
#
def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')


    dbconnect = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root@#$1234',
        database='codeplanet'
    )

    crs = dbconnect.cursor()

    query = "select password from user_applicant_info where email='" + email + "'"

    crs.execute(query)

    data= crs.fetchone()
    str=''
    if data is None:
        str='you are not registered now'
    else:
        if data[0]==password:
            str='you are valid user'
        else:
            str='your password is not correct'
    return HttpResponse(str)

def view_job_detail(request):
    jobs = []
    queryset = Job.objects.all()
    for job in queryset:
        job_data = {
            'id': job.id,
            'title': job.title,
            'company_name': job.company_name,
            'salary': job.salary,
            'description': job.description,
            'location': job.location,
            'skills': job.skills,
            'date_posted': job.date_posted,
        }
        jobs.append(job_data)
    return HttpResponse(jobs)


def search_jobs(request):
    location = request.GET.get('location')
    title = request.GET.get('title')
    company_name = request.GET.get('company_name')

    dbconnect = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root@#$1234',
        database='codeplanet'
    )

    crs = dbconnect.cursor()

    if location:
        sql_query = 'SELECT * FROM recruiter_job WHERE location=%s'
        crs.execute(sql_query, (location,))
    elif title:
        sql_query = 'SELECT * FROM recruiter_job WHERE title=%s'
        crs.execute(sql_query, (title,))
    elif company_name:
        sql_query = 'SELECT * FROM recruiter_job WHERE company_name=%s'
        crs.execute(sql_query, (company_name,))
    else:
        # If no search parameters are provided, return all jobs
        sql_query = 'SELECT * FROM recruiter_job'
        crs.execute(sql_query)

    jobs = crs.fetchall()

    job_dicts = []
    for job in jobs:
        job_dict = {
            'id': job[0],
            'title': job[1],
            'company_name': job[2],
            'description': job[3],
            'location': job[4],
            'skills': job[5],
            'salary': job[6],
            'start_date': job[7],
            'end_date': job[8]
        }
        job_dicts.append(job_dict)
    return HttpResponse(job_dicts)


def job_apply(request,job_id):
    current_time = timezone.now()
    job = Job.objects.get(id=job_id)
    end_date = datetime.datetime.combine(job.end_date, datetime.time.min)
    end_date = timezone.make_aware(end_date, timezone.get_current_timezone())
    if current_time > end_date:
        return HttpResponse('Sorry the application deadline has passed')

    if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            address=request.POST.get('address')
            contact_info=request.POST.get('contact_info')
            work_experience=request.POST.get('work_experience')
            education=request.POST.get('education')
            skills=request.POST.get('skills')
            resume=request.FILES.get('resume')


            try:
                Applicant_info.objects.get(email=email)
            except Applicant_info.DoesNotExist:
                return HttpResponse('Please sign up before applying')

            if JobApplicationform.objects.filter(email=email).exists():
                return HttpResponse('You have already applied to this job')

            j=JobApplicationform(name=name,email=email,address=address,contact_info=contact_info,work_experience=work_experience,education=education,skills=skills, resume=resume)


            j.save()
            return HttpResponse('Your application has been submitted successfully')
    return HttpResponse('<h1>successfully done ,check more info on postman</h1>')

