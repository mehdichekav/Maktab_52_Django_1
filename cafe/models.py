from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone




def menu_Item_price_validator(value):
    if value < 0:
        raise ValidationError('menu item price can')


class Table(models.Model):
    # orders = models.IntegerField()
    table_number = models.IntegerField( help_text='enter your Table')
    cafe_space_position = models.CharField(max_length=30)

    # @classmethod
    # def total_price(self):
    #     return sum(map(lambda o:o.get_final_price(),self.orders.all()))




class MenuItemAdmin:
    pass


class category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, help_text='enter your menu')


class MenuItem(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, help_text='enter your menu')
    price = models.IntegerField(help_text='enetr the price(cant)', verbose_name='price(toman)',
                                validators=[menu_Item_price_validator])
    Discount = models.IntegerField(help_text='enter the Discount', verbose_name='Discount', default=0)
    Image = models.ImageField(upload_to='images/', blank=True, null=True)

    category = models.ForeignKey(Table, on_delete=models.CASCADE)
    create_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='date', name='date_f')
    modify_timestamp = models.DateTimeField(auto_now=True, verbose_name='date_time', name='date_t')

    def __str__(self):
        return f'{self.id}#  {self.name} : {self.price}'

    # @classmethod
    # def max_price(cls):
    #     return cls.objects.aggregate(models.max('price'))


class Orders(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_items = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    number = models.IntegerField()
    status = models.fields.CharField(max_length=30)

    # def get_final_price(self):
    #     return 10

    # @classmethod
    # def filter_by_menuitem(cls, menu_item):
    #     return cls.objects.filter(menu_items=menu_item)
    #
    # @classmethod
    # def filter_by_category(cls, category):
    #     return cls.objects.filter(menu_items__category=category)
    #
    # @classmethod
    # def sum_cost(cls):
    #     return cls.objects.filter(table__table_number__exact=...)
    #
    # @classmethod
    # def today_orders(cls, deliver_date__day=None):
    #     return cls.objects.filter(deliver_date__day=timezone.now().day)
    #
    # @classmethod
    # def month_orders(cls, deliver_date__day=None):
    #     return cls.objects.filter(deliver_date__day=timezone.now().month)
    #
    #





class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    birthday = models.DateField()

    def __str__(self):
        return self.first_name


class Receipts(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    final_price = models.IntegerField()
    time_stamp = models.TimeField()

