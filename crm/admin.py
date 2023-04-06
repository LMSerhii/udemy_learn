from django.contrib import admin
from .models import Order, CrmStatus, CommentCrm


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 1  # количество полей


# класс для кастомизации админки
class OrderAdm(admin.ModelAdmin):
    list_display = ('id',
                    'order_status',
                    'order_name',
                    'order_phone',
                    'order_dt')  # какие колонки будут отображаться в админке согласно модели

    list_display_links = ('id',
                          'order_name')  # Определяет кликабельные поля

    search_fields = ('id',
                     'order_name',
                     'order_phone',
                     'order_dt')  # виджет поиска

    list_filter = ('order_status',)  # Виджет фильтра

    list_editable = ('order_status', 'order_phone')  # возможность редактирования не заходя в заказ

    list_per_page = 10  # Сколько заказов на странице

    list_max_show_all = 100  # максимальное количество показов

    fields = ('id', 'order_dt', 'order_status', 'order_name', 'order_phone',)  # порядок отображения

    readonly_fields = ('id', 'order_dt')  # указываем поля только для чтения для тех которые не могут редактироваться

    # Поле класса коммент
    inlines = [Comment, ]  # в списке передаем классы которые будут отображаться в данном


admin.site.register(Order, OrderAdm)
admin.site.register(CrmStatus)
admin.site.register(CommentCrm)
