import httpx
from typing import Any, Dict

from fcm_box.clients.base import BaseHTTPClient

class httpxSyncClient(BaseHTTPClient):
    """Synchronous HTTP client implementation using the HTTPX library."""

    def __init__(self, base_url: str, headers: Dict[str, str], timeout: int = 5):
        """Initialize the client and set up the persistent synchronous session."""
        super().__init__(base_url, headers, timeout)
        self._client = httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            timeout=self.timeout
        )

    def post(self, endpoint: str, json_data: Dict[str, Any]) -> Dict[str, Any]:
        """Send a synchronous POST request with internal exception handling."""
        try:
            response = self._client.post(endpoint, json=json_data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP status error: {e.response.status_code}", "data": json_data}
        except httpx.RequestError as e:
            return {"error": f"Network request error: {str(e)}", "data": json_data}

    def close(self) -> None:
        """Close the underlying HTTPX client session."""
        self._client.close()

    def __enter__(self) -> "httpxSyncClient":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()
