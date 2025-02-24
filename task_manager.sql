CREATE DATABASE task_management;
USE task_management;

-- Create Users Table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,  -- Fixed column name
    name VARCHAR(100) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    role ENUM('admin', 'manager', 'employee') NOT NULL  -- Standardized ENUM values
);

-- Insert Sample Users
INSERT INTO users (name, email, role) VALUES
('Alice Johnson', 'alice@example.com', 'manager'),
('Bob Smith', 'bob@example.com', 'employee'),
('Charlie Davis', 'charlie@example.com', 'admin');

-- Create Tasks Table
CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
    priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deadline DATE
);

-- Insert Sample Tasks
INSERT INTO tasks (title, description, status, priority, deadline) VALUES
('Complete Report', 'Submit Q1 report', 'Pending', 'High', '2025-03-15'),
('Update Website', 'Revamp homepage UI', 'In Progress', 'Medium', '2025-04-10');

-- Create Task Assignments Table
CREATE TABLE task_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    task_id INT,
    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id) ON DELETE CASCADE
);

-- Insert Task Assignments
INSERT INTO task_assignments (user_id, task_id) VALUES
(1, 1),  -- Alice assigned "Complete Report"
(2, 2);  -- Bob assigned "Update Website"
