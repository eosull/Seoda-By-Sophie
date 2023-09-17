from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    # Handle Stripe Webhooks

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # Handle a webhook event

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        # Handle payment intent succeeded webhook from Stripe

        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billling_details = intent.charges.data[0].billling_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # Clean shipping data
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile info if save_info checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number__iexact = shipping_details.phone_number
                profile.default_country__iexact = shipping_details.country
                profile.default_postcode__iexact = shipping_details.postcode
                profile.default_town_or_city__iexact = shipping_details.town_or_city
                profile.default_street_address1__iexact = shipping_details.street_address1
                profile.default_street_address2__iexact = shipping_details.street_address2
                profile.default_county__iexact = shipping_details.county
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone_number,
                    country__iexact=shipping_details.country,
                    postcode__iexact=shipping_details.postcode,
                    town_or_city__iexact=shipping_details.town_or_city,
                    street_address1__iexact=shipping_details.street_address1,
                    street_address2__iexact=shipping_details.street_address2,
                    county__iexact=shipping_details.county,
                    grand_total=shipping_details.grand_total,
                    original_bag=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200
                )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=shipping_details.email,
                    phone_number=shipping_details.phone_number,
                    country=shipping_details.country,
                    postcode=shipping_details.postcode,
                    town_or_city=shipping_details.town_or_city,
                    street_address1=shipping_details.street_address1,
                    street_address2=shipping_details.street_address2,
                    county=shipping_details.county,
                    original_bag=basket,
                    stripe_pid=pid,
                )
                for product_id, quantity in json.loads(basket).items():
                    product = Product.objects.get(id=product_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

    def handle_payment_intent_payment_failed(self, event):
        # Handle a payment intent failed webhook from Stripe

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200
        )
