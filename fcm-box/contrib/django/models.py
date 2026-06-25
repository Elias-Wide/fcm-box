from django.db import models

from fcm_box/core/constants import PLATFORM_ANDROID, PLATFORM_CHOICES
from fcm_core.contrib.base_device import BaseFCMDevice


class AbstractFCMDevice(models.Model, BaseFCMDevice):
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
        return f"FCM Device {self.id} ({self.platform})"

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.save(update_fields=["is_active"])
