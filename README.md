# HR ERP Management System

A full-stack HR ERP web application built using Flask and MySQL to manage employee records and HR operations.

## Features
- Admin Login (Session Based)
- Add Employee
- View Employee Records
- Search Employee
- Update Employee Details
- Delete Employee
- Secure Admin Dashboard

## Tech Stack
- Backend: Flask (Python)
- Database: MySQL
- Frontend: HTML, CSS
- Authentication: Flask Sessions

## Project Structure
- Modular templates using Jinja
- Secure parameterized SQL queries
- CRUD operations implemented

## How to Run
1. Clone the repository
2. Install dependencies:
3. Import database from `database/hr_erp_db.sql`
4. Run the application:
5. Open browser and go to:
http://127.0.0.1:5000/


## Author
**Narendra Paswan**

Proper Folder Structure
HR-ERP-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── header.html
│   ├── adminheader.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── adminlogin.html
│   ├── admindas.html
│   ├── addemploy.html
│   ├── showemploy.html
│   ├── searchemploy.html
│   ├── profile.html
│   ├── update.html
│   ├── delete.html
│   └── admin_registration_succes.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── database/
    └── hr_erp_db.sql

