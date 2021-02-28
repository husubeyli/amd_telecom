from django.apps import AppConfig


class ContactConfig(AppConfig):
    name = 'contact'

    def ready(self):
        import contact.signals