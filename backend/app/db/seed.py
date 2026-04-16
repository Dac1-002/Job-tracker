import asyncio
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.db.enums import ApplicationStatus
from app.db.models.application import Application
from app.db.models.company import Company
from app.db.models.contact import Contact
from app.db.models.reminder import Reminder
from app.db.models.status_history import StatusHistory
from app.db.models.user import User

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def seed():
    async with SessionLocal() as session:
        # -------------------
        # 1 USER
        # -------------------
        user = User(name="Test User", email="test@example.com")

        session.add(user)
        await session.commit()
        await session.refresh(user)

        # -------------------
        # 3 COMPANIES
        # -------------------
        companies = [
            Company(name="Google"),
            Company(name="Microsoft"),
            Company(name="Amazon"),
        ]

        session.add_all(companies)
        await session.commit()

        for c in companies:
            await session.refresh(c)

        # -------------------
        # 5 APPLICATIONS
        # -------------------
        applications = [
            Application(
                user_id=user.id,
                company_id=companies[0].id,
                position="Backend Developer",
                status=ApplicationStatus.APPLIED,
            ),
            Application(
                user_id=user.id,
                company_id=companies[1].id,
                position="Frontend Developer",
                status=ApplicationStatus.INTERVIEWING,
            ),
            Application(
                user_id=user.id,
                company_id=companies[2].id,
                position="Full Stack Developer",
                status=ApplicationStatus.REJECTED,
            ),
            Application(
                user_id=user.id,
                company_id=companies[0].id,
                position="Data Engineer",
                status=ApplicationStatus.OFFERED,
            ),
            Application(
                user_id=user.id,
                company_id=companies[1].id,
                position="DevOps Engineer",
                status=ApplicationStatus.APPLIED,
            ),
        ]

        session.add_all(applications)
        await session.commit()

        for a in applications:
            await session.refresh(a)

        # -------------------
        # STATUS HISTORY (2 per application)
        # -------------------
        status_history = []

        for app in applications:
            status_history.append(
                StatusHistory(application_id=app.id, status="CREATED")
            )
            status_history.append(
                StatusHistory(application_id=app.id, status=app.status.value)
            )

        session.add_all(status_history)

        # -------------------
        # CONTACTS (2)
        # -------------------
        contacts = [
            Contact(
                user_id=user.id,
                company_id=companies[0].id,
                name="John Recruiter",
                email="john@google.com",
            ),
            Contact(
                user_id=user.id,
                company_id=companies[1].id,
                name="Sarah HR",
                email="sarah@microsoft.com",
            ),
        ]

        session.add_all(contacts)

        # -------------------
        # REMINDERS (2)
        # -------------------
        reminders = [
            Reminder(
                application_id=applications[0].id,
                note="Follow up email",
                remind_at=datetime.utcnow() + timedelta(days=3),
            ),
            Reminder(
                application_id=applications[1].id,
                note="Prepare interview",
                remind_at=datetime.utcnow() + timedelta(days=1),
            ),
        ]

        session.add_all(reminders)

        await session.commit()

        print("🌱 Database seeded successfully!")


if __name__ == "__main__":
    asyncio.run(seed())
