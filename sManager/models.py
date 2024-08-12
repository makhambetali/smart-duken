from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Supplier(models.Model):
    name = models.CharField('Название', max_length=50)
    supervisor = models.CharField(
        'Супервайзер', max_length=20, blank=True, null=True)
    tel_number_supervisor = models.CharField(
        'Номер Телефона (супервайзер)', max_length=20, blank=True, null=True)
    extra_info = models.TextField('Доп. информация',blank=True, null=True)
    salesman = models.CharField(
        'Торговый Представитель', max_length=20, blank=True, null=True)
    tel_number_salesman = models.CharField(
        'Номер Телефона (торг. представитель)', max_length=20, blank=True, null=True)
    delivery = models.CharField(
        'Доставка', max_length=20, blank=True, null=True)
    tel_number_delivery = models.CharField(
        'Номер Телефона (Доставка)', max_length=20, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField('Время публикации', auto_now=True)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Поставщика'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    STATUS_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Банковский счёт'),
        ('mix', 'Смешанная оплата'),
    ]
    name = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    cost = models.CharField(max_length=9)
    # cost_masked = models.CharField(
    #     max_length=9, verbose_name='Сумма:', help_text="Минимальная сумма: 10тг")  # ₸ 999.999
    bonus = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='Бонус:')
    exchange = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='Обмен:')
    comment = models.TextField(
        null=True, blank=True, verbose_name='Комментарии:')
    date = models.DateField(default=None)
    confirmed = models.BooleanField(default=False, null=True, blank=True)
    payment = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='cash')
    date_added = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    cash_amount = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Наличка:')
    transfer_amount = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Банковский счёт:')
    def __str__(self) -> str:   
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставку'
        verbose_name_plural = 'Поставки'


class ProductImages(models.Model):
    supply = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images")
    images = models.FileField(upload_to='images/')

class Profile(models.Model):
    profile = models.ForeignKey(User, on_delete = models.CASCADE, null=False, blank = False)
    image = models.ImageField(upload_to='users_images/', default="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/510px-Default_pfp.svg.png?20220226140232")


class Client(models.Model):
    name = models.CharField('Имя Клиента',max_length=20)
    phone_number = models.CharField('Номер Телефона',max_length=20, blank=True, null=True)
    about = models.TextField('Доп. информация',blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    is_chosen = models.BooleanField('Избранный',blank=True, null=True, default=False)
    def __str__(self) -> str:
         return self.name

    @property
    def debt_sum(self):
        debts = self.debt_set.all()
        sum_value = 0
        for debt in debts:
            try:
                sum_value += eval(debt.content)
            except:
                pass
        return sum_value

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Debt(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.CharField('Операция', max_length=10)
    description = models.TextField('Доп. информация', blank=True, null=True, default='')

    date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Update last_modified of the associated client
        self.client.last_modified = datetime.now()
        self.client.save()

    def __str__(self):
        return f'{self.client} : {self.content}'

    def get_creation_date(self):
        return self.date.strftime('%d-%m-%Y %H:%M:%S')  # Формат даты по вашему выбору


    class Meta:
        verbose_name = 'Долг'
        verbose_name_plural = 'Долги'

class Money(models.Model):
    content = models.CharField('Операция',max_length=10)
    text = models.TextField('Доп. информация',blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.content}'
    
class FinanceRecord(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=0)
    cash_amount = models.DecimalField(max_digits=10, decimal_places=0) 
    transfer_amount = models.DecimalField(max_digits=10, decimal_places=0)
    income = models.DecimalField(max_digits=10, decimal_places=0)
    expense = models.DecimalField(max_digits=10, decimal_places=0)
    date = models.DateField()
    def __str__(self):
        return f"{self.date}"