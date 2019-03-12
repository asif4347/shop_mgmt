from django.db import models

# Create your models here.
from django.urls import reverse


class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class Salesman(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    shops = models.ManyToManyField(Shop, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    com = 'Completed'
    pro = 'In Progress'
    choice = (
        (pro, "In progress"),
        (com, 'completed'),
    )
    salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=25,choices=choice)
    total_amount = models.IntegerField()
    amount_paid = models.IntegerField(null=True, default=0)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('edit_order', kwargs={'pk': self.pk})


class Amount(models.Model):
    delivery = models.ForeignKey(Orders, on_delete=models.CASCADE)
    timestamp = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):

        super(Amount, self).save(*args, **kwargs)


class OrderProducts(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


    def __str__(self):
            return str(self.order.id)



# class Profile(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     created_date = models.DateTimeField(default=timezone.now)
#
#     def get_absolute_url(self):
#         return reverse('profile-update', kwargs={'pk': self.pk})
#
#     def __unicode__(self):
#         return "%s %s" % (self.first_name, self.last_name)
#
#
# class FamilyMember(models.Model):
#     profile = models.ForeignKey(Profile)
#     name = models.CharField(max_length=100)
#     relationship = models.CharField(max_length=100)
