from django.core.management.base import BaseCommand
from test3.models import Student
import random

class Command(BaseCommand):
    help = "Populate the students table with sample data"

    def handle(self, *args, **kwargs):
        # Xóa dữ liệu cũ
        Student.objects.all().delete()

        # Các lớp với số lượng học sinh khác nhau
        class_data = [
            (5, 35),  # 5 lớp, mỗi lớp có 35 học sinh
            (6, 45),  # 6 lớp, mỗi lớp có 45 học sinh
            (10, 30), # 10 lớp, mỗi lớp có 30 học sinh
            (4, 40),  # 4 lớp, mỗi lớp có 40 học sinh
        ]

        class_number = 1
        for num_classes, num_students in class_data:
            for _ in range(num_classes):
                for _ in range(num_students):
                    # Tuổi của học sinh trong khoảng 18-23
                    age = round(random.uniform(18, 23), 1)
                    Student.objects.create(class_number=class_number, age=age)
                class_number += 1

        self.stdout.write(self.style.SUCCESS("Successfully populated the database with students data"))
