from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base
from app.db.enums import ApplicationStatus


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    position = Column(String, nullable=True)
    status = Column(SQLAlchemyEnum(ApplicationStatus), nullable=False, default=ApplicationStatus.APPLIED)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="applications")
    company = relationship("Company", back_populates="applications")
    status_history = relationship("StatusHistory", back_populates="application")
    documents = relationship("Document", back_populates="application")
    reminders = relationship("Reminder", back_populates="application")