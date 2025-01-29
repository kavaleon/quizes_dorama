from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    image = models.ImageField(blank=True)
    num_questions = models.IntegerField()
    genre = models.CharField(max_length=20)

class Question(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    genre = models.CharField(max_length=20)
    answer1 = models.CharField(max_length=30)
    answer2 = models.CharField(max_length=30)
    answer3 = models.CharField(max_length=30)
    answer_r = models.CharField(max_length=30)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

class User(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)