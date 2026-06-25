rom abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


class BaseFCMDevice(ABC):
    """
    Abstract interface for FCM device management.

    This class provides architectural blueprint for device storage fields and
    lifecycle methods. It guarantees that specific task runner mechanisms
    can safely access infrastructure fields (like token and state flags)
    across different Python frameworks without hard coupling.

    Attributes:
        id (Any): Database primary key identifier.
        registration_token (str): Firebase unique registration identifier.
        platform (Any): Hardware architecture type restricted by configuration.
        is_active (bool): Operation flag routing traffic strictly away.
        created_at (datetime): Database engine commit timestamp.
        updated_at (datetime): Internal state modification tracker.
    """

    id: Any
    registration_token: str
    platform: Any
    is_active: bool
    created_at: datetime
    updated_at: datetime

    @abstractmethod
    def deactivate(self) -> None:
        """
        Flips the status flag to False to isolate non-routable devices.

        This method must be triggered natively upon receiving 404
        exceptions from Firebase REST infrastructure.
        """
        pass
