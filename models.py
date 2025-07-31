from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON
from database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, index=True)
    recipient = Column(String, index=True)
    timestamp = Column(DateTime)
    type = Column(String)
    payload = Column(JSON)
    delivered = Column(Boolean, default=False, nullable=False)
