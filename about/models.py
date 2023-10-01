# Models for About categories, faqs and testimonials

from django.db import models
from products.models import Product


# Category model for faq and contact submissions
class InfoCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Info Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=False, blank=False,
                                   default='Category description')

    # Methods to return category name and friendly name
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Question and answer model for FAQs
class Faq(models.Model):
    class Meta:
        verbose_name_plural = 'FAQs'

    category = models.ForeignKey('InfoCategory', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Method to return Faq question
    def __str__(self):
        return self.question


# Testimonial Model for displaying customer reviews
class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'

    customer = models.CharField(max_length=254, null=True, blank=True)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    testimonial = models.TextField(null=False, blank=True)

    # Return summary of testimonial
    def __str__(self):
        return f'{self.customer} thoughts on {self.product.name}'

