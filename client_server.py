from typing import List, Dict, Any
from datetime import datetime
import requests
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# --- Message Pydantic Schema ---
class MessageSchema(BaseModel):
    sender: str
    recipient: str
    timestamp: datetime
    type: str
    payload: Dict[str, Any]

    class Config:
        from_attributes = True

# --- A2A Client ---
class A2AClient:
    def __init__(self, base_url: str, agent_id: str):
        self.base_url = base_url.rstrip("/")
        self.agent_id = agent_id

    def send(self, to: str, type: str, payload: Dict[str, Any]) -> MessageSchema:
        msg = MessageSchema(
            sender=self.agent_id,
            recipient=to,
            timestamp=datetime.utcnow(),
            type=type,
            payload=payload
        )
        resp = requests.post(f"{self.base_url}/messages", json=msg.model_dump(mode='json'))
        resp.raise_for_status()
        return MessageSchema(**resp.json())

    def fetch(self) -> List[MessageSchema]:
        resp = requests.get(
            f"{self.base_url}/messages", params={"recipient": self.agent_id}
        )
        resp.raise_for_status()
        data = resp.json()
        return [MessageSchema(**m) for m in data]

# --- A2A Server (FastAPI) ---
app = FastAPI()

# --- Dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/messages", response_model=MessageSchema)
def post_message(msg: MessageSchema, db: Session = Depends(get_db)):
    """Receive a message and store it for recipients to fetch."""
    db_msg = models.Message(**msg.model_dump())
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg

@app.get("/messages", response_model=List[MessageSchema])
def get_messages(recipient: str, db: Session = Depends(get_db)):
    """Retrieve and mark as delivered pending messages for a given recipient."""
    pending = db.query(models.Message).with_for_update().filter(
        models.Message.recipient == recipient,
        models.Message.delivered == False
    ).all()

    for msg in pending:
        msg.delivered = True

    db.commit()

    return pending

# --- Run the server ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
