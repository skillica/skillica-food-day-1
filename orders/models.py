from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    # name varchar(50)
    price = models.PositiveIntegerField()
    # price int
    quantity = models.PositiveIntegerField(default=0)
    # quantity int default 0

    def __str__(self):
        return f"{self.name} (LKR {self.price})"


class Combo(models.Model):
    items = models.CharField(max_length=150)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"Combo {self.pk}"


class Extra(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    extras = models.ManyToManyField(Extra)
    delivery_method = models.CharField(
        max_length=20,
        choices=(
            ("pickup", "Pick Up"),
            ("home_delivery", "Home Delivery"),
        ),
    )
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.pk} - {self.full_name}"
