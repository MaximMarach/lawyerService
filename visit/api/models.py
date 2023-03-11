from django.db import models


class Contact(models.Model):

    first_name = models.CharField(verbose_name='Имя пользователя', 
                                max_length=50, 
                                blank=False)
    
    second_name = models.CharField(verbose_name='Фамилия пользователя', 
                                    max_length=50, 
                                    blank=True)
    
    email = models.CharField(verbose_name='Почта', 
                            max_length=255, 
                            blank=True)

    phone_number = models.CharField(verbose_name='Номер телефона',
                                    max_length=255,
                                    blank=True)
    
    description = models.TextField(verbose_name='Описание проблемы', blank=False)

    date_of_call = models.DateField(verbose_name='Дата заявки', auto_now_add=True)

    is_checked = models.BooleanField(verbose_name='Прошел ли консультацию?', default=False)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        db_table = 'request'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['date_of_call']
