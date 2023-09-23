from django.db import models
from products.models import Product


class InfoCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Info Categories'
    
    # Category model for faq and contact submissions
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=False, blank=False, default='Category description')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Faq(models.Model):
    class Meta:
        verbose_name_plural = 'FAQs'

    # Question and answer model for answering FAQs
    category = models.ForeignKey('InfoCategory', null=True, blank=True, on_delete=models.SET_NULL)
    question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'

    # Testimonial Model for submitting customer thoughts
    customer = models.CharField(max_length=254, null=True, blank=True)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    testimonial = models.TextField(null=False, blank=True)

    def __str__(self):
        return f'{self.customer} thoughts on {self.product.name}'

