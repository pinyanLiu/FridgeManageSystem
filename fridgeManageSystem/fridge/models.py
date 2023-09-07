from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHICES = (
        ('M','Male'),
        ('F','Female'),
        ('R','Rather not to tell'),
    )

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length = 1, choices=GENDER_CHICES)
    birthday = models.DateTimeField()
    mail = models.EmailField()
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Item(models.Model):
    owner = models.ManyToManyField(User)
    name = models.CharField(max_length = 100)
    dueDate = models.DateTimeField()
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name
