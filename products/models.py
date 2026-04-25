from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    telugu_name = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=500, blank=True)
    farmer_id = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user_id')

    def __str__(self):
        return f"Review by {self.user_name} on {self.product.name}"
