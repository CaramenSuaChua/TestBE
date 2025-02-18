from django.core.management.base import BaseCommand
from test4.models import Person
import random

class Command(BaseCommand):
    help = "Populate the database with people data"

    def handle(self, *args, **kwargs):
        # Xóa dữ liệu cũ
        Person.objects.all().delete()

        for _ in range(10000):  # 10,000 người
            age = random.randint(1, 100)  # Tuổi từ 1 - 100
            name = f"Person_{random.randint(1, 10000)}"
            Person.objects.create(name=name, age=age)

        self.stdout.write(self.style.SUCCESS("Successfully populated database with 10,000 people"))
