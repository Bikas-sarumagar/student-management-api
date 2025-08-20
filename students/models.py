from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.PositiveIntegerField(unique = True)
    student_class = models.CharField(max_length=50)
    dob = models.DateField()
    
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["roll"]
        
    def __str__(self):
        return f"{self.roll} - {self.name}"