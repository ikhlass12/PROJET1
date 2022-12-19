from django.core.mail import send_mail
from django.db import models
from pynput.keyboard import Key, Controller
class Dht(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):

        if self.temp<2 :
            #envoyer un message sur telegrame
            import telepot
            token = '5844251477:AAFqGvHUzMLymXwAPbmINdP69kEXajPanFc'
            rece_id = 1957979316
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, 'Attention temperature severe ! la temperature est a '+ str(self.temp))
            #envoyer un message sur email
            send_mail(
                'Attention ! température severe,' + str(self.temp),
                'anomalie dans la machine',
                'ikhlas.elormi@ump.ac.ma',
                ['ikhlaselhormi@gmail.com'],
                fail_silently=False)
            #envoyer un message sur whatssap
            import pywhatkit as kit
            kit.sendwhatmsg_instantly(f'+212653275305', "You are special in my heart, sweetie. Forever will you, darling.",15,True)
            keyboard=Controller()
            keyboard.press(Key.enter)

        return super().save(*args, **kwargs)




