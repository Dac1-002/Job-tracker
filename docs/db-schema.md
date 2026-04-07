# Database Schema

This document describes the database structure for our project. It explains each table, its purpose, and how it relates to other tables.

## Tables

### 1. users
- **Purpose: Stores** information about the users of the system.
- **Why it exists:** We need to know who is submitting applications, writing comments, etc.
- **Columns:**
  - `id` (PK): Unique identifier for each user
  - `name`: Full name of the user
  - `email`: User’s email address

### 2. companies
- **Purpose:** Stores information about companies.
- **Why it exists:** Users apply to these companies and jobs belong to them.
- **Columns:**
  - `id` (PK): Unique identifier for each company
  - `name`: Company name
  - `industry`: Type of industry

### 3. applications
- **Purpose:** Tracks job applications submitted by users.
- **Why it exists:** Connects users to companies they applied to.
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

### 5. jobs
- **Purpose:** Stores job openings for companies.
- **Why it exists:** Allows users to see and apply to jobs.
- **Columns:**
  - `id` (PK): Unique identifier for each job
  - `title`: Job title
  - `company_id` (FK): References the company offering the job
  - `description`: Job description

### 6. comments
- **Purpose:** Stores user comments on applications.
- **Why it exists:** Enables discussion or notes related to an application.
- **Columns:**
  - `id` (PK): Unique identifier for each comment
  - `application_id` (FK): References the application the comment belongs to
  - `user_id` (FK): References the user who wrote the comment
  - `content`: The comment text
  - `created_on`: Date of creation

### 7. documents
- **Purpose:** Stores documents attached to applications (e.g., resume, cover letter).
- **Why it exists:** Keeps track of all files submitted with applications.
- **Columns:**
  - `id` (PK): Unique identifier for each document
  - `application_id` (FK): References the application this document belongs to
  - `filename`: Name of the file
  - `url`: Location where the file is stored

## ER Diagram

```mermaid
erDiagram
    users {
        int id PK
        string name
        string email
    }
    companies {
        int id PK
        string name
        string industry
    }
    applications {
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
    jobs {
        int id PK
        string title
        int company_id FK
        string description
    }
    comments {
        int id PK
        int application_id FK
        int user_id FK
        string content
        date created_on
    }
    documents {
        int id PK
        int application_id FK
        string filename
        string url
    }

    users ||--o{ applications : "owns"
    applications ||--|| companies : "applies to"
    applications ||--o{ status_history : "has"
    companies ||--o{ jobs : "offers"
    users ||--o{ comments : "writes"
    applications ||--o{ comments : "has"
    applications ||--o{ documents : "includes"