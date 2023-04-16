import uuid
from django.db import models

class Course_Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()

    def __str__(self):
        return self.title

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.TextField()
    title = models.TextField()
    type = models.ForeignKey(Course_Type, on_delete=models.PROTECT)

    def __str__(self):
        return "<Course " + self.code + ">"

class Exam_Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()

    def __str__(self):
        return self.title


class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    type = models.ForeignKey(Exam_Type, on_delete=models.PROTECT)

    def __str__(self):
        return "<Exam " + self.title + ">"