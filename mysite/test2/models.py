from django.db import models

class HtmlFile(models.Model):
    system = models.CharField(max_length=100)
    environment = models.CharField(max_length=50)
    machine_number = models.IntegerField()
    machine_level = models.IntegerField()
    filename = models.CharField(max_length=255)
    file_path = models.TextField()

    def __str__(self):
        return f"{self.system}/{self.environment}/{self.machine_number}/{self.filename}"
