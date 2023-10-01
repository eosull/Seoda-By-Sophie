from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # Tell app to listen out for signals
    def ready(self):
        import checkout.signals
