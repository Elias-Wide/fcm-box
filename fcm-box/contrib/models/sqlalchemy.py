from datetime import datetime

from sqlalchemy import Boolean, DateTime, Enum, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from fcm_box.core.constants import PlatformEnum
from fcm_box.core.contrib.models import BaseFCMDevice


class FCMDeviceMixin(BaseFCMDevice):
    """
    SQLAlchemy mixin for FCM device registration.

    Provides database schema fields mapping device infrastructure to modern
    declarative engines. Integrates natively with background routines to
    invalidate tokens on upstream protocol rejections.

    Attributes:
        id (int): Database record key.
        registration_token (str): Firebase tracking sequence.
        platform (PlatformEnum): Device operating system ecosystem.
        is_active (bool): Invalidation switch flag.
        created_at (datetime): Database initialization record.
        updated_at (datetime): Last structural update event.
    """

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    registration_token: Mapped[str] = mapped_column(
        Text, unique=True, nullable=False
    )
    platform: Mapped[PlatformEnum] = mapped_column(
        Enum(PlatformEnum), default=PlatformEnum.ANDROID, nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def deactivate(self):
        """
        Switches the device active property state to disabled.
        """
        if self.is_active:
            self.is_active = False
