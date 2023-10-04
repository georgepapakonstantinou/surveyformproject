from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to= 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username


class Patient(models.Model):

    IDENTITY = models.CharField(max_length=10,null=True)
    EDUCCATEGORY = models.CharField(max_length=100,null=True)
    EDUCPATIENT = models.CharField(max_length=100,null=True)
    SEXPATIENT = models.CharField(max_length=100,null=True)
    AGEPATIENT = models.CharField(max_length=10,null=True)
    ECUCCARERCAT = models.CharField(max_length=100,null=True)
    EDUCCARER = models.CharField(max_length=100,null=True)
    SEXCARER = models.CharField(max_length=100,null=True)
    AGECARER = models.CharField(max_length=100,null=True)
    RELATIONSHIPCARER = models.CharField(max_length=100,null=True)
    LIVESIN = models.CharField(max_length=100,null=True)
    kentro = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)
    NPI = models.CharField(max_length=100,null=True)
    STAGE = models.CharField(max_length=100,null=True)
    IADL = models.CharField(max_length=100,null=True)
    MMSE = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.id} {self.IDENTITY}"



class Question(models.Model):
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    notes = models.CharField(max_length=200,null=True)
    first_answer = models.CharField(max_length=10)
    second_answer = models.CharField(max_length=10,null=True)


    def __str__(self):
        return f"{self.patient} answered question {self.question.id} : {self.first_answer}"
