from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass



from app.db.models.user import User
from app.db.models.company import Company
from app.db.models.application import Application
from app.db.models.status_history import StatusHistory
from app.db.models.contact import Contact
from app.db.models.document import Document
from app.db.models.reminder import Reminder