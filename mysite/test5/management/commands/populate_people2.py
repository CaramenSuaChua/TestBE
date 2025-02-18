from django.core.management.base import BaseCommand
from test5.models import Person
import random

class Command(BaseCommand):
    help = "Populate database with random people positions"

    def handle(self, *args, **kwargs):
        # Xóa dữ liệu cũ
        Person.objects.all().delete()

        for i in range(1000):  # 1,000 người
            x = random.uniform(-100, 100)  # X nằm trong khoảng -100 đến 100
            y = random.uniform(-100, 100)  # Y nằm trong khoảng -100 đến 100
            name = f"Person_{i+1}"
            Person.objects.create(name=name, x=x, y=y)

        self.stdout.write(self.style.SUCCESS("Successfully populated database with 1000 people"))
