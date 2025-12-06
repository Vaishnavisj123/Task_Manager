✅ Task Manager System

A complete Task Management System built using:

MySQL (backend database)

Streamlit (interactive web UI)

Python (task operations & session state management)

This project allows users to add tasks, update tasks, view tasks, and search tasks, while also providing a structured SQL backend for real-world task assignment and user management.

🧱 1. Project Components

🔹 1. MySQL Database (task_manager.sql)

This SQL file sets up the database with 3 tables:

Table	Description
users	Stores user information (admin/manager/employee)
tasks	Stores tasks with priority, status, description, deadline
task_assignments	Maps tasks to users

It also includes sample users, sample tasks, and assignments.

🔹 2. Streamlit App (task_manager2.py)

A clean and modern web-based task manager with:

Add Task

Update Task

View All Tasks

Search Tasks

The app stores tasks using Streamlit Session State, so no external database is needed for running the interface.

💡 Features

✔ Database Features (MySQL)

Create Users (admin, manager, employee)

Create Tasks with priority (Low/Medium/High)

Assign tasks to users

Automatic timestamps

Preloaded sample data

✔ Streamlit App Features

➕ Add Task

Set Task ID

Description

Due date (calendar input)

Priority (High/Medium/Low)

🔄 Update Task

Update status (Pending / In Progress / Completed)

Update due date

📋 View All Tasks

Shows:

Task ID

Description

Status

Priority

Due date

Days remaining

🔍 Search Task

Search by:

Description

Status
(e.g., “Completed”, “Pending”, “report”, etc.)

🛠️ 2. MySQL Database Schema (Summary)

Below tables are created:

✔ users
✔ tasks
✔ task_assignments

Sample Users (from SQL file):

Name	Email	Role
Alice Johnson	alice@example.com
	manager
Bob Smith	bob@example.com
	employee
Charlie Davis	charlie@example.com
	admin

Sample Tasks:

Title	Status	Priority
Complete Report	Pending	High
Update Website	In Progress	Medium

🧩 3. Streamlit Code Overview

The Streamlit script contains:

📌 Class: TaskManager

Handles logic for:

Adding tasks

Updating tasks

Viewing tasks

Searching tasks

📌 UI: Tabs for Easy Navigation

The app uses 4 tabs:

Tab	Function
Add Task	Insert a new task
Update Task	Modify existing task
View Tasks	Display all tasks
Search Task	Search by keyword/status

▶️ 4. How to Run the Streamlit App

Step 1 — Install Required Libraries
pip install streamlit

Step 2 — Run the App
streamlit run task_manager2.py


✔ Your browser will open with the Task Manager UI.

🗄️ 5. How to Use the MySQL Database

Step 1 — Import SQL File

Run this in MySQL Workbench / phpMyAdmin / CLI:

SOURCE task_manager.sql;


This will create:

Database: task_management

Tables: users, tasks, task_assignments

Sample data

Step 2 — Connect your backend (optional)

If you want, I can help you create:

✔ Python API (FastAPI / Flask)
✔ Admin Dashboard (Streamlit + MySQL)
✔ Authentication System

Just tell me!

✔ 6. Folder Structure

TaskManagerProject/
│── task_manager.sql        # MySQL database file
│── task_manager2.py        # Streamlit frontend app
│── README.md               # Project documentation

🎯 7. Future Enhancements

Link Streamlit app directly to MySQL

Add user login authentication

Add task comments & attachments

Add analytics dashboard (charts, stats)

Add email reminders for deadlines
