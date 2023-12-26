from django.db import models
from django.utils import timezone


class Manufacturer(models.Model):
    """ Модель производителя """

    title = models.CharField(max_length=200, verbose_name='Производитель', unique=True)
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=200, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Номер дома')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Supplier(models.Model):
    """ Модель поставщика """
    DISTRIBUTOR = 'торговая сеть'
    IE = 'ИП'

    supplier_type = (
        (DISTRIBUTOR, 'торговая сеть'),
        (IE, 'ИП')
    )

    title = models.CharField(max_length=200, verbose_name='Производитель', unique=True)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    type = models.CharField(choices=supplier_type, verbose_name='Тип поставщика')
    country = models.CharField(max_length=200, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Номер дома')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    """Модель товара"""

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')
    title = models.CharField(max_length=200, verbose_name='Название товара')
    model = models.CharField(max_length=200, verbose_name='Модель товара')
    release_date = models.DateTimeField(default=timezone.now, verbose_name='Дата выхода товара на рынок')

    def __str__(self):
        return f'{self.title} - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supply(models.Model):
    """Модель поставки"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')
    supplier = models.ForeignKey(Supplier, related_name='related_supplier', on_delete=models.CASCADE,
                                 verbose_name='Поставщик', null=True, blank=True)
    recipient = models.ForeignKey(Supplier, related_name='related_recipient', on_delete=models.CASCADE,
                                  verbose_name='Получатель поставки', null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f'{self.product}, производитель {self.manufacturer}, поставщик {self.supplier}, '
                f'получатель {self.recipient}, дата {self.created_at}')

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'






