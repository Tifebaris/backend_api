from django.apps import AppConfig



class SmsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SMS_App'


    # def ready(self):
    #     from . import signals
