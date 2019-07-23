from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    address = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=70, blank=True)
    customer_image = models.FileField(blank=True, null=True, verbose_name="Add Photo to Customer")

    def __str__(self):
        return '{} {}: {}'.format(self.first_name, self.last_name, self.phone_number)


class Provider(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    article_image = models.FileField(blank=True, null=True, verbose_name="Add logo")

    def __str__(self):
        return self.name


class Product(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name="Provider", related_name="products")
    name = models.CharField(max_length=100, verbose_name="name")
    content = RichTextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_image = models.FileField(blank=True, null=True, verbose_name="Add Photo to product")

    def __str__(self):
        return '{} ({}), закупка: {}грн'.format(self.name, self.provider, self.price)


class Deal(models.Model):
    deal_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer", related_name="deal")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product", related_name="deal")
    deal_price = models.DecimalField(max_digits=6, decimal_places=2)
    profit = models.DecimalField(max_digits=6, null=True, decimal_places=2)

    def __str__(self):
        return '{}, {}, {}'.format(self.deal_date, self.customer, self.product)

    class Meta:
        ordering = ['-deal_date']



