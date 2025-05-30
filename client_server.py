from typing import List, Dict, Any
from datetime import datetime
import requests
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

# --- Message Model ---
class Message(BaseModel):
    sender: str
    recipient: str
    timestamp: datetime
    type: str  # e.g., "command", "response", "status"
    payload: Dict[str, Any]

# --- A2A Client ---
class A2AClient:
    def __init__(self, base_url: str, agent_id: str):
        self.base_url = base_url.rstrip("/")
        self.agent_id = agent_id

    def send(self, to: str, type: str, payload: Dict[str, Any]) -> Message:
        msg = Message(
            sender=self.agent_id,
            recipient=to,
            timestamp=datetime.utcnow(),
            type=type,
            payload=payload
        )
        resp = requests.post(f"{self.base_url}/messages", json=msg.dict())
        resp.raise_for_status()
        return Message(**resp.json())

    def fetch(self) -> List[Message]:
        resp = requests.get(
            f"{self.base_url}/messages", params={"recipient": self.agent_id}
        )
        resp.raise_for_status()
        data = resp.json()
        return [Message(**m) for m in data]

# --- A2A Server (FastAPI) ---
app = FastAPI()

# In-memory store for messages
_messages: List[Dict[str, Any]] = []

@app.post("/messages")
def post_message(msg: Message):
    """Receive a message and store it for recipients to fetch."""
    _messages.append(msg.dict())
    return msg.dict()

@app.get("/messages")
def get_messages(recipient: str) -> List[Message]:
    """Retrieve and remove pending messages for a given recipient."""
    pending = [m for m in _messages if m["recipient"] == recipient]
    # Remove delivered messages
    for m in pending:
        _messages.remove(m)
    return pending

# --- Run the server ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
