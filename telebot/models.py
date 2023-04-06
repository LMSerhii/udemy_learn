from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='token')
    tg_chat = models.CharField(max_length=200, verbose_name='chat_id')
    tg_message = models.TextField(verbose_name='message')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'