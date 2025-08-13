from httpx import AsyncClient, Timeout

http_client = AsyncClient(http2=True, timeout=Timeout(5))
