# Student Attendance Management System

A web-based Student Attendance Management System built using Python, Django, MySQL, HTML, CSS, and JavaScript.

## Project Overview

This application helps manage student records and attendance through a web interface. It provides features for maintaining student information, recording attendance, reviewing attendance history, and exporting attendance reports.

## Technologies Used

- **Backend:** Python, Django
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Report Export:** Excel

## Features

- Student registration and management
- Add, view, edit, and delete student records
- Attendance management by department, class, and date
- Attendance history and filtering
- Attendance summary
- Export attendance reports to Excel for administrators
- User management
- Password reset functionality
- Login and authentication

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/nandhini-2211/Student-Attendance-Management-System---Project.git
cd Student-Attendance-Management-System---Project
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies

Install the packages required by the project:

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure the required settings, including:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `GMAIL_ADDRESS`
- `GMAIL_APP_PASSWORD`

Use your own local configuration. Never upload your `.env` file or expose passwords and secret keys publicly.

### 5. Create the MySQL database

Create a MySQL database named `student_management`, or use the database name configured in your `.env` file.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Security Note

Keep database credentials, email app passwords, and Django secret keys in environment variables. Do not commit sensitive configuration files to GitHub.

## Author

Developed as a full-stack web application project using Python and Django.
