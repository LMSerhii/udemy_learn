from django.db import models


class CrmStatus(models.Model):
    crm_status = models.CharField(max_length=100, verbose_name='Название статуса')

    def __str__(self):
        return self.crm_status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(CrmStatus, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Комментарий')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.comment_text[:50]}..."

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'