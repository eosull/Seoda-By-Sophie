from django.db import models
from products.models import Product


class Faq(models.Model):
    # Question and answer model for answering FAQs
    question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Testimonial(models.Model):
    # Testimonial Model for submitting customer thoughts
    customer = models.CharField(max_length=254, null=True, blank=True)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    testimonial = models.TextField(null=False, blank=True)

    def __str__(self):
        return f'{self.customer} thoughts on {self.product.name}'

