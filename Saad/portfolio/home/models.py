from django.db import models


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year = models.IntegerField()


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
