from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=100)
    duration=models.CharField(max_length=50, default='3 months')
    about_course = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


GENGER_CHOICE=(
    ('M', 'male'),
    ('F', 'female')
)
class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.DateField()
    gender=models.CharField(max_length=2, choices=GENGER_CHOICE)
    email = models.EmailField(max_length=100)
    contact = models.BigIntegerField()
    address = models.TextField()


    def __str__(self):
        return self.firstname + " " + self.lastname
    
class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE )
    is_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.student} registered"
    

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    course_assigned = models.ForeignKey(Course, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=GENGER_CHOICE)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name



 
