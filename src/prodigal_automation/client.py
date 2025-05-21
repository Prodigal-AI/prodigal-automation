import os
import requests
from prodigal_automation.auth import require_token

class ProdigalClient:
    def __init__(self, base_url: str, token: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.token = token or os.getenv("PRODIGAL_TOKEN")

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def enqueue(self, agent_id: str, payload: dict):
        resp = requests.post(
            f"{self.base_url}/enqueue",
            json={"agent_id": agent_id, "payload": payload},
            headers=self._headers(),
        )
        resp.raise_for_status()
        return resp.json()
