from django.db import models

# Create your models here.

#STATUS_CHOICES= (("pending","Pending"),("accepted","Accepted"),("rejected","Rejected"))

class recruiter_info(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    company_name= models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    # confirm_password=models.CharField(max_length=50)
    active_status=models.CharField(max_length=50,default="pending")#choices=STATUS_CHOICES)
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

class Job(models.Model):
    title = models.CharField(max_length=200)
    company_name= models.CharField(max_length=200)
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=400)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    is_appoved=models.BooleanField(default=False)