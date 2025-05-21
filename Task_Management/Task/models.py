from django.db import models
from Category.models import categories

# Create your models here.
class AddTask(models.Model):
    tasktitle = models.CharField(max_length=200)
    taskdescription = models.TextField()
    iscomplete = models.BooleanField("Mark as Complete", default=False)
    assigndate = models.DateTimeField()
    category = models.ManyToManyField(categories)

    def __str__(self):
        return self.tasktitle