from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField("Название курса", max_length=100)
    start_date = models.DateTimeField('Начало курса')
    duration = models.CharField("Длительность курса", max_length=50)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name


class Mentors(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    about = models.TextField()
    course = models.ManyToManyField(Course)
    position = models.ForeignKey('Position', on_delete=models.DO_NOTHING, verbose_name='Должность')

    def __str__(self):
        return f"{self.name} {self.surname}"


class Position(models.Model):
    title = models.CharField('Должность', max_length=100)

    def __str__(self):
        return self.title


class Claim(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Номер телефона', max_length=50)
    email = models.CharField('Почта', max_length=50)

    def __str__(self):
        return self.name
