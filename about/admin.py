from django.contrib import admin
from .models import InfoCategory, Faq, Testimonial


class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'created',
        'updated',
    )

    ordering = ('-updated',)


class InfoCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'product',
    )


admin.site.register(Faq, FaqAdmin)
admin.site.register(InfoCategory, InfoCategoryAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
