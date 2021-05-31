from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    """Model definition for Contact."""

    # informations
    first_name = models.CharField("First name", max_length=50, null=False)
    last_name = models.CharField("Last name", max_length=50, null=False)
    phone_number = PhoneNumberField(null=False, max_length=14, region="AZ")
    email = models.EmailField("Email", max_length=254, null=False)
    message = models.TextField("Message", null=False)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        """Meta definition for Contact."""
        db_table = "Contact"
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ('-created_at',)

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.get_fullname()


    # def get_absolute_url(self):
    #     """Return absolute url for Contact."""
    #     return ('')

