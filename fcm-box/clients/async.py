import httpx
from typing import Any, Dict
from .base import BaseHTTPClient


class httpxAsyncClient(BaseHTTPClient):
    """Asynchronous HTTP client implementation leveraging async HTTPX engine."""

    def __init__(self, base_url: str, headers: Dict[str, str], timeout: int = 5):
        """Configure client environment building unconstrained execution connections layout."""
        super().__init__(base_url, headers, timeout)
        limits = httpx.Limits(max_keepalive_connections=None, max_connections=None)
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=self.headers,
            timeout=self.timeout,
            limits=limits
        )

    async def post(self, endpoint: str, json_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform non-blocking coroutine POST run and raise exceptions on HTTP errors."""
        response = await self._client.post(endpoint, json=json_data)
        response.raise_for_status()
        return response.json()

    async def close(self) -> None:
        """Terminate the underlying concurrent operational pipeline cleanly."""
        await self._client.aclose()

    async def __aenter__(self) -> "httpxAsyncClient":
        """Enter the asynchronous runtime context related to this object."""
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Exit the asynchronous runtime context and close the underlying client."""
        await self.close()
