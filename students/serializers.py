from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "roll","student_class", "dob", "created_At","updated_At"]
        read_only_fields = ["id","created_At", "updated_At"]
        