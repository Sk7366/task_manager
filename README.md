# Task Manager CLI

A lightweight, modular, and efficient Command Line Interface (CLI) Task Manager built with Python. This application enables users to create, manage, update, and organize tasks directly from the terminal while leveraging SQLite for persistent data storage.

Designed with a modular architecture, the project demonstrates clean code organization, object-oriented programming principles, and database integration, making it an excellent showcase of Python application development.

---

## Features

- Create new tasks
- View all existing tasks
- Update task details
- Mark tasks as completed
- Delete tasks
- Persistent data storage using SQLite
- Input validation for improved reliability
- Modular and maintainable codebase
- Interactive command-line interface

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Core Programming Language |
| SQLite | Local Database |
| OOP | Application Design |
| CLI | User Interface |

---

## Project Structure

```text
task_manager/
│
├── cli/
│   ├── interface.py
│   └── __init__.py
│
├── database/
│   ├── db_manager.py
│   ├── tasks.db
│   └── __init__.py
│
├── models/
│   ├── task.py
│   └── __init__.py
│
├── utils/
│   ├── validators.py
│   └── __init__.py
│
├── main.py
├── README.md
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.9 or later
- Git

### Installation

Clone the repository

```bash
git clone https://github.com/Sk7366/task_manager.git
```

Navigate into the project directory

```bash
cd task_manager
```

Run the application

```bash
python main.py
```

---

## Application Workflow

```text
Start Application
        │
        ▼
 Display Main Menu
        │
        ▼
Select an Operation
        │
        ├── Add Task
        ├── View Tasks
        ├── Update Task
        ├── Complete Task
        ├── Delete Task
        └── Exit
        │
        ▼
 Update SQLite Database
        │
        ▼
 Display Updated Results
```

---

## Core Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Modular Programming
- SQLite Database Integration
- CRUD Operations
- Command-Line Interface Design
- Data Validation
- Python Package Organization

---

## Future Enhancements

- Task priorities
- Due dates and reminders
- Categories and tags
- Search and filtering
- Sorting tasks
- Colored terminal output
- Export tasks to CSV or JSON
- Backup and restore functionality
- User authentication
- Unit testing with PyTest


## Learning Outcomes

This project demonstrates practical experience with:

- Building modular Python applications
- Designing maintainable software architecture
- Implementing CRUD operations with SQLite
- Applying object-oriented programming principles
- Creating interactive command-line applications
- Organizing scalable project structures

---

## Author

**SaiKirti Krishnan**

Computer Science Engineering (AI & ML) Student

GitHub: https://github.com/Sk7366

---

## License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star.
