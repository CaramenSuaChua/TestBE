from django.db import models

class Student(models.Model):
    class_number = models.IntegerField()  # Số thứ tự lớp
    age = models.FloatField()  # Tuổi của học sinh
