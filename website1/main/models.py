from django.db import models
from datetime import date

class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')
    # deadline = models.DateField('Дата окончания', null=True, blank=False)
    exec_time = models.TextField('Укажите время выполнения', default='')
    # author = models.CharField('Автор', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
