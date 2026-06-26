pythonfrom abc import ABC, abstractmethod
from typing import Any, Dict


class BaseHTTPClient(ABC):
    """Abstract base class defining the contract for HTTP clients."""

    def __init__(self, base_url: str, headers: Dict[str, str], timeout: int = 5):
        """Initialize the HTTP client with connection settings.

        Args:
            base_url (str): The base target URL for requests.
            headers (dict): HTTP headers to include in every request.
            timeout (int): Request timeout in seconds. Defaults to 5.
        """
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout
