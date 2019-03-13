from django.db import models
import datetime

class user_info(models.Model):

    id_card = models.CharField('id_card',max_length=200, default=None, primary_key=True)
    user_name = models.CharField('user_name', max_length=200,default=None,) 
    phone_number = models.IntegerField('phone_number', default=None) 
    regist_times = models.DateTimeField('regist_times', default=datetime.datetime.now())
    #this part is set up for the forms. Talk about it later.....
    def __str__(self):
        return self.id_card