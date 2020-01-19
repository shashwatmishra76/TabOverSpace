from django.db import models
# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Subdomain(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Question(models.Model):
    subdomain = models.ForeignKey(Subdomain, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Question Title',
                             null=True)
    question_body = models.TextField(max_length=500, verbose_name='Details',
                                     null=True)
    input_format = models.TextField(max_length=500,
                                    verbose_name='Expected Input',
                                    null=True)
    output_format = models.TextField(max_length=500,
                                     verbose_name='Expected Output',
                                     null=True)
    sample_input = models.TextField(max_length=500,
                                    verbose_name='Sample Input Format',
                                     null=True)
    sample_output = models.TextField(max_length=500,
                                     verbose_name='Sample Output Format',
                                     null=True)
    explanation = models.TextField(max_length=1000,
                                   verbose_name='I/O Explanation',
                                   null=True)

    def __str__(self):
        return self.title or str(self.id)


class TestCases(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='Test Case Number')
    input = models.TextField(max_length=2000,
                             verbose_name='Test Case Input',
                             null=True)
    output = models.TextField(max_length=2000,
                              verbose_name='Test Case Output',
                              null=True)

    def __str__(self):
        return f'{self.question_id} Test Case #{self.number}'
