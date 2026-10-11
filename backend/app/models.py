from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Objective(Base):
    __tablename__ = "objectives"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    owner = Column(String)
    quarter = Column(String, index=True)
    created_at = Column(DateTime, server_default=func.now())
    key_results = relationship("KeyResult", back_populates="objective")

class KeyResult(Base):
    __tablename__ = "key_results"
    id = Column(Integer, primary_key=True)
    objective_id = Column(Integer, ForeignKey("objectives.id"))
    title = Column(String, nullable=False)
    target = Column(Float, default=100.0)
    current = Column(Float, default=0.0)
    unit = Column(String, default="%")
    objective = relationship("Objective", back_populates="key_results")

    @property
    def progress(self):
        return min(1.0, self.current / self.target) if self.target else 0.0
