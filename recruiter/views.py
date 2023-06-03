
from django.http import HttpResponse, HttpResponseBadRequest
import mysql.connector

from recruiter.models import Job

from user.models import Applicant_info


def signup(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        username=request.POST.get('username')
        company_name=request.POST.get('company_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        active_status=request.POST.get('active_status')

        dbconnect=mysql.connector.connect(
            host='localhost',
            user='root',
            password='Root@#$1234',
            database='codeplanet'
        )

        crs=dbconnect.cursor()

        query="select * from recruiter_recruiter_info  where email= '"+email+"'"

        crs.execute(query)

        data=crs.fetchone()

        if data is None:
            query = "insert into recruiter_recruiter_info values('"+id+"','"+username+"','"+company_name+"','"+email+"','"+password+"','"+active_status+"')"

            crs.execute(query)

            dbconnect.commit()
            return HttpResponse("recruiter registration successfully completed")
        else:
            return HttpResponse("you are already registered")


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

    query = "select password from recruiter_recruiter_info where email='" + email + "'"

    crs.execute(query)

    data= crs.fetchone()
    str=''
    if data is None:
        str='you are not registered now'
    else:
        if data[0]==password:
            str='you are valid recruiter'
        else:
            str='your password is not correct'
    return HttpResponse(str)

def create_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        company_name = request.POST.get('company_name')
        salary = request.POST.get('salary')
        location = request.POST.get('location')
        skills = request.POST.get('skills')
        description = request.POST.get('description')
        start_date=request.POST.get('start_date')
        end_date= request.POST.get('end_date')


        j=Job(title=title,company_name=company_name,salary=salary,location=location
              ,skills=skills,description=description,start_date=start_date,end_date=end_date)
        j.save()
    return HttpResponse('job created successfully')

#
# def job_list(request):
#     jobs = []
#     dbconnect = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='Root@#$1234',
#         database='codeplanet'
#     )
#
#     crs = dbconnect.cursor()
#
#     query = "SELECT * FROM recruiter_job"
#
#     crs.execute(query)
#     rows = crs.fetchall()
#     for row in rows:
#         Job = {
#             'id':row[0],
#             'title': row[1],
#             'company_name':row[2],
#             'salary':row[3],
#             'description': row[4],
#             'location': row[5],
#             'skills': row[6],
#             'date_posted':row[7]
#         }
#         jobs.append(Job)
#     return HttpResponse(jobs)

def job_list(request):
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
#





def delete_job(request):
    id= request.GET.get('id')
    # import  pdb;pdb.set_trace()
    obj = Job.objects.get(id=id)
    obj.delete()
    return HttpResponse('Job deleted successfully')

# def update_job(request):
#     id = request.GET.get('id')
#     title=request.GET.get('title')
#     company_name=request.GET.get('company_name')
#     description=request.GET.get('description')
#     location=request.GET.get('location')
#     skill=request.GET.get('skill')
#     salary=request.GET.get('salary')
#     start_date=request.GET.get('start_date')
#     end_date=request.GET.get('end_date')
#
#
#     job = Job.objects.get(id=id)
#
#     #Update job fields
#     job.title = title
#     job.company_name = company_name
#     job.description = description
#     job.location = location
#     job.skills = skill
#     job.salary=salary
#     job.start_date= start_date
#     job.end_date=end_date
#
#     job.save()
#     return HttpResponse('Job updated successfully')


def update_job(request, id):
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        return HttpResponseBadRequest("Invalid Job id")

    # Update job fields if provided in request
    if 'title' in request.GET:
        job.title = request.GET['title']
    if 'company_name' in request.GET:
        job.company_name = request.GET['company_name']
    if 'description' in request.GET:
        job.description = request.GET['description']
    if 'location' in request.GET:
        job.location = request.GET['location']
    if 'skill' in request.GET:
        job.skills = request.GET['skill']
    if 'salary' in request.GET:
        job.salary = request.GET['salary']
    if 'start_date' in request.GET:
        job.start_date = request.GET['start_date']
    if 'end_date' in request.GET:
        job.end_date = request.GET['end_date']

    job.save()
    return HttpResponse('Job updated successfully')


def view_all_applicant(request):
    applicants = []
    queryset = Applicant_info.objects.all()
    for applicant in queryset:
        applicant_data = {
            'id': applicant.id,
            'username': applicant.username,
            'email': applicant.email,
            'password': applicant.password,
            'confirm_password': applicant.confirm_password,
            'active_status': applicant.active_status
        }
        applicants.append(applicant_data)
    return HttpResponse(applicants)

