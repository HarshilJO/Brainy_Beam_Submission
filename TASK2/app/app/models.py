from django.db import models

class DataFrameEntry(models.Model):
    column1 = models.CharField(max_length=255)
    column2 = models.CharField(max_length=255)
    column3 = models.CharField(max_length=255)
    date_field = models.DateField()

    def __str__(self):
        return f"{self.column1} - {self.date_field}"