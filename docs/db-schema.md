# Database Schema

This document describes the database structure for our project. It explains each table, its purpose, and how it relates to other tables.

## Tables

### 1. user
- **Purpose:** Stores information about the users of the system.
- **Why it exists:** We need to know who is submitting applications, adding contacts, uploading documents, or setting reminders.
- **Columns:**
  - `id` (PK): Unique identifier for each user
  - `name`: Full name of the user
  - `email`: User’s email address

### 2. company
- **Purpose:** Stores information about companies.
- **Why it exists:** Users apply to these companies, and applications reference them.
- **Columns:**
  - `id` (PK): Unique identifier for each company
  - `name`: Company name
  - `industry`: Type of industry

### 3. application
- **Purpose:** Tracks job applications submitted by users.
- **Why it exists:** Connects users to companies they applied to and serves as the central point for related contacts, documents, reminders, and status history.
- **Columns:**
  - `id` (PK): Unique identifier for each application
  - `user_id` (FK): References the user who submitted the application
  - `company_id` (FK): References the company the application was sent to
  - `applied_on`: Date of application

### 4. status_history
- **Purpose:** Tracks the history of statuses for each application (e.g., pending, interviewed, rejected).
- **Why it exists:** Helps monitor application progress over time.
- **Columns:**
  - `id` (PK): Unique identifier for each status update
  - `application_id` (FK): References the application this status belongs to
  - `status`: Status description
  - `updated_on`: Date when the status was updated

### 5. contact
- **Purpose:** Stores contact information related to a specific application (e.g., recruiter or company representative).
- **Why it exists:** Each application may involve a contact person for communication or follow-ups.
- **Columns:**
  - `id` (PK): Unique identifier for each contact
  - `application_id` (FK): References the application this contact belongs to
  - `name`: Name of the contact person
  - `email`: Email address of the contact
  - `phone`: Phone number of the contact

### 6. document
- **Purpose:** Stores documents attached to applications (e.g., resume, cover letter).
- **Why it exists:** Keeps track of all files submitted with applications.
- **Columns:**
  - `id` (PK): Unique identifier for each document
  - `application_id` (FK): References the application this document belongs to
  - `filename`: Name of the file
  - `url`: Location where the file is stored

### 7. reminder
- **Purpose:** Stores reminders or notifications related to applications.
- **Why it exists:** Helps users track important dates, such as follow-ups or interviews.
- **Columns:**
  - `id` (PK): Unique identifier for each reminder
  - `application_id` (FK): References the application this reminder is for
  - `message`: Reminder message
  - `remind_on`: Date when the reminder should trigger

## ER Diagram

```mermaid
erDiagram
    user {
        int id PK
        string name
        string email
    }
    company {
        int id PK
        string name
        string industry
    }
    application {
        int id PK
        int user_id FK
        int company_id FK
        date applied_on
    }
    status_history {
        int id PK
        int application_id FK
        string status
        date updated_on
    }
    contact {
        int id PK
        int application_id FK
        string name
        string email
        string phone
    }
    document {
        int id PK
        int application_id FK
        string filename
        string url
    }
    reminder {
        int id PK
        int application_id FK
        string message
        date remind_on
    }

    user ||--o{ application : "owns"
    application ||--|| company : "applies to"
    application ||--o{ status_history : "has"
    application ||--o{ contact : "has"
    application ||--o{ document : "includes"
    application ||--o{ reminder : "has"