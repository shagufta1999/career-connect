from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import mysql.connector

from user.models import Applicant_info

from recruiter.models import recruiter_info


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        dbconnect = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Root@#$1234',
            database='codeplanet'
        )

        crs = dbconnect.cursor()

        query = "select * from admin_portal_admin where username= '" + username + "'"

        crs.execute(query)

        data = crs.fetchone()

        if data is None:
            # query = "insert into admin_portal_admin values('" + username + "','" + password + "')"
            query = "insert into admin_portal_admin (username, password) values ('" + username + "','" + password + "')"

            crs.execute(query)

            if username == "admin" and password == "123":
                return HttpResponse("Login successful")
            else:
                return HttpResponse("Invalid credentials")
            dbconnect.commit()
        else:
            return HttpResponse('invalid method')



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

def view_all_recruiter(request):
    recruiters = []
    queryset = recruiter_info.objects.all()
    for recruiter in queryset:
        recruiter_data = {
            'id': recruiter.id,
            'username': recruiter.username,
            'company_name':recruiter.company_name,
            'email':recruiter.email,
            'password':recruiter.password,
            'active_status': recruiter.active_status
        }
        recruiters.append(recruiter_data)
    return HttpResponse(recruiters)

def delete_applicant(request):
    id= request.GET.get('id')
    obj = Applicant_info.objects.get(id=id)
    obj.delete()
    return HttpResponse('applicant deleted successfully')



def delete_recruiter(request):
    id= request.GET.get('id')
    obj = recruiter_info.objects.get(id=id)
    obj.delete()
    return HttpResponse('recruiter deleted successfully')

#
# def view_pending_recruiters(request):
#     dbconnect = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='Root@#$1234',
#         database='codeplanet'
#     )
#     cur = dbconnect.cursor()
#
#     query="SELECT * FROM recruiter_recruiter_info  WHERE active_status='pending'"
#     cur.execute(query)
#     rows = cur.fetchall()
#     recruiters = []
#     for row in rows:
#         recruiter = {
#
#             'id': row[0],
#             'username': row[1],
#             'company_name': row[2],
#             'email': row[3],
#             'password': row[4],
#             'active_status': row[5],
#         }
#         recruiters.append(recruiter)
#
#     return HttpResponse(recruiters)



def change_status(request):
    dbconnect = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root@#$1234',
        database='codeplanet'
    )
    cur = dbconnect.cursor()
    id=request.GET.get('id')
    query="update recruiter_recruiter_info set active_status='active' where id= %s"
    data=(id,)
    cur.execute(query, data)
    dbconnect.commit()
    return HttpResponse('Recruiter updated_active successfully ')


def rejected_change_status(request):
    dbconnect = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root@#$1234',
        database='codeplanet'
    )
    cur = dbconnect.cursor()
    id=request.GET.get('id')
    query="update recruiter_recruiter_info set active_status='rejected' where id= %s"
    data=(id,)
    cur.execute(query, data)
    dbconnect.commit()
    return HttpResponse('Recruiter rejected')



def view_pending_recruiters(request):
    data = recruiter_info.objects.filter(active_status='pending').values()
    return HttpResponse(list(data))


def view_active_recruiter(request):
    data = recruiter_info.objects.filter(active_status='active').values()
    return HttpResponse(list(data))

def view_rejected_recruiter(request):
    data = recruiter_info.objects.filter(active_status='rejected').values()
    return HttpResponse(list(data))



def is_approval_job(request):
    dbconnect = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root@#$1234',
        database='codeplanet'
    )
    cur = dbconnect.cursor()
    id=request.GET.get('id')
    query="update  recruiter_job set is_appoved=True where id= %s"
    data=(id,)
    cur.execute(query, data)
    dbconnect.commit()
    return HttpResponse('approval done')