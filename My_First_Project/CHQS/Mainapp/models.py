from djongo import models

from django.urls import reverse

#Create your models here.
class Student(models.Model):

    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Memo(models.Model):

    mem_stu_name = models.ForeignKey(Student, related_name = 'records',on_delete=models.CASCADE)
    mem_sora = models.CharField(max_length=50)
    mem_from = models.IntegerField()
    mem_to = models.IntegerField()
    mem_date = models.DateField()
    mem_quant = models.IntegerField()
    mem_rmrk = models.CharField(max_length=20)
    mem_finished = models.CharField(max_length=50)

    def __str__(self):
        return self.mem_stu_name, self.mem_sora, self.mem_from, self.mem_to