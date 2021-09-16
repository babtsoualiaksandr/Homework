from django.db import models


class Task(models.Model):
    number = models.IntegerField(blank=False)
    describe = models.CharField(max_length=200, blank=False)
    input = models.CharField(max_length=200, blank=False)
    function_name = models.CharField(max_length=30, blank=False)
    result = models.CharField(max_length=200, blank=False)
    date = models.DateField(blank=True, default=None)
    def __str__(self):
        return f'Task № {self.number} {self.describe} {self.input} {self.function_name}'
    
