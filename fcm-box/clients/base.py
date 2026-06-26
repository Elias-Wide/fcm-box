from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseHTTPClient(ABC):
    """Abstract base class handling common network configurations for HTTP clients."""

    def __init__(self, base_url: str, headers: Dict[str, str], timeout: int = 5):
        """Initialize the HTTP client with network configurations.

        Args:
            base_url (str): The base target URL for requests.
            headers (dict): HTTP headers to include in every request.
            timeout (int): Request timeout in seconds. Defaults to 5.
        """
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout

    @abstractmethod
    def post(self, endpoint: str, json_data: Dict[str, Any]) -> Any:
        """Execute a POST request against the designated endpoint.

        Args:
            endpoint (str): API action destination path or direct complete URI.
            json_data (dict): Primary object payload body transmitted inside request.
        """
        pass
