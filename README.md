# HR Portal - Flask & MySQL

A simple HR Portal application for managing employees using Flask and MySQL.

## Project Structure

```
.
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── db.py                  # Database initialization and connection
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── templates/             # HTML templates
    ├── base.html          # Base template with styling
    ├── index.html         # Employee list page
    ├── add_employee.html  # Add employee form
    └── edit_employee.html # Edit employee form
```

## Features

- View all employees
- Add new employee
- Edit employee information
- Delete employee
- Simple and clean UI

## Prerequisites

### Pour Docker (Recommandé)
- Docker
- Docker Compose

### Pour Installation Locale
- Python 3.7+
- MySQL Server installed and running
- pip (Python package manager)

## Setup Instructions

### Option 1: Docker (Recommandé)

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd bts-int-portailrh-apps
```

#### 2. Lancer avec Docker Compose

```bash
docker-compose up --build
```

L'application sera disponible sur `http://localhost:5000`

### Option 2: Installation Locale

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd bts-int-portailrh-apps
```

#### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Configure Database Connection

Edit the `.env` file with your MySQL credentials:

```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password_here
MYSQL_DATABASE=hr_portal
MYSQL_PORT=3306
DEBUG=True
```

#### 4. Initialize the Database

Run the following command to create the database and tables:

```bash
python app.py init
```

#### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

### View Employees
- Go to the home page to see all employees listed in a table

### Add Employee
- Click "+ Add Employee" button
- Fill in the employee details (required fields are marked with *)
- Click "Add Employee" to save

### Edit Employee
- Click "Edit" button next to any employee
- Update the information
- Click "Update Employee" to save changes

### Delete Employee
- Click "Delete" button next to any employee
- Confirm the deletion

## Database Schema

The application uses a single `employees` table with the following structure:

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    position VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    hire_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## Notes

- This is a simple demo application
- Change the `app.secret_key` in `app.py` for production use
- Make sure MySQL server is running before starting the application
- The application uses MySQL connector for Python

## Development Branch

Please use the `dev` branch for development.
