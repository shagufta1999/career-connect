from django.db import models

# Create your models here.
class Applicant_info(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    active_status=models.BooleanField(default=True)
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username



WORK_EXPERIENCE_CHOICES = (
    ('0-1', 'Less than 1 year'),
    ('1-2', '1-2 years'),
    ('2-5', '2-5 years'),
    ('5-10', '5-10 years'),
    ('10+', 'More than 10 years'),
)

EDUCATION_CHOICES = (
    ('high_school', 'High School'),
    ('bachelors', 'Bachelor\'s Degree'),
    ('masters', 'Master\'s Degree'),
    ('phd', 'PhD'),
    ('other', 'Other'),
)
SKILLS_CHOICES = (
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('java', 'Java'),
    ('csharp', 'C#'),
    ('php', 'PHP'),
    ('ruby', 'Ruby'),
    ('other', 'Other'),
)

class JobApplicationform(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=50)
    work_experience = models.CharField(max_length=100, choices=WORK_EXPERIENCE_CHOICES)
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    skills = models.CharField(max_length=20, choices=SKILLS_CHOICES)
    # image = models.ImageField()
    resume = models.FileField()

    def __str__(self):
        return self.name
