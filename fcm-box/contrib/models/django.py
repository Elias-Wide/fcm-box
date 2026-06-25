from django.db import models

from fcm_box.core.constants import PLATFORM_ANDROID, PLATFORM_CHOICES
from fcm_core.contrib.base_device import BaseFCMDevice


class AbstractFCMDevice(models.Model, BaseFCMDevice):
    """
    Abstract device model for Django ORM integration.

    Acts as a base class to construct local token registration tables.
    Does not create an independent database table on its own.
    """

    registration_token = models.TextField(
        unique=True, verbose_name="FCM Token"
    )
    platform = models.CharField(
        max_length=15,
        choices=PLATFORM_CHOICES,
        default=PLATFORM_ANDROID,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        """
        Returns string representation of the registered device.
        """
        return f"FCM Device {self.id} ({self.platform})"

    def deactivate(self):
        """
        Disables the device and persists state changes to the database.
        """
        if self.is_active:
            self.is_active = False
            self.save(update_fields=["is_active"])

