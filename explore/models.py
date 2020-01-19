from django.db import models

# Create your models here.
class Subtopic(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Article(models.Model):
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    article = models.CharField(max_length=500)

    def __str__(self):
        return self.article
