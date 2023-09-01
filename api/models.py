from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=250, default='')
    instructor = models.CharField(max_length=100, default='')
    instructorIcon= models.ImageField(upload_to='api/instructor-icons/', default='')
    icon = models.ImageField(upload_to='api/course-icons/', default='')

    def __str__(self):
        return self.title


