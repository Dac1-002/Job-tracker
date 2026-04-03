# Architecture Overview 

This project is a simple web application made of a frontend (what the user sees), a backend (the logic), and some services that help store data and run the app.

Everything works together so the user can open a website, interact with it, and see results.

---

## 1. Browser / React SPA

This is the part the user sees and uses.

It runs in the browser (like Chrome) and is built with React. It shows buttons, pages, and data.

When the user clicks something, this part sends a request to the backend to get or send data.

---

## 2. Azure Static Web Apps

This is where the frontend is hosted.

It stores the React app and sends it to the user’s browser when they open the website.

So when someone visits your site, this service loads the app for them.

---

## 3. Azure App Service (FastAPI)

This is the backend (the “brain” of the app).

It receives requests from the frontend and decides what to do.

For example:
- get data from the database
- save new data
- process user actions

Then it sends a response back to the frontend.

---

## 4. Azure Container Registry

This is where we store the backend as a Docker image.

Think of it like a storage place for the packaged version of your backend.

Azure App Service takes the backend from here and runs it.

---

## 5. Azure Database for PostgreSQL

This is where the app stores important data.

Examples:
- users
- tasks
- any saved information

The backend talks to the database to read and write data.

---

## 6. Azure Blob Storage

This is used for storing files.

Examples:
- images
- uploads
- large files

The backend saves and gets files from here.

---

## How Everything Works Together

1. The user opens the website in their browser.
2. Azure Static Web Apps sends the frontend (React app).
3. The user clicks something.
4. The frontend sends a request to the backend.
5. The backend:
   - talks to the database (for data)
   - talks to storage (for files)
6. The backend sends a response back.
7. The frontend updates what the user sees.

---

## Simple Summary

- Frontend = what you see
- Backend = what does the work
- Database = where data is saved
- Storage = where files are saved

All parts connect to make the app work.


## Architecture Diagram

```mermaid
flowchart LR

    Browser["Browser / React SPA"]
    Static["Azure Static Web Apps"]
    App["Azure App Service (FastAPI)"]
    DB["Azure Database for PostgreSQL"]
    Blob["Azure Blob Storage"]
    Registry["Azure Container Registry"]

    Browser --> Static
    Static --> App
    App --> DB
    App --> Blob
    Registry --> App

    