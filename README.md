# 📝 Login & To-Do Application

A web-based Login and To-Do application developed using Python, Flask, MySQL, HTML, CSS, and JavaScript as part of **Introduction to Database Systems — Lab 2**.

The application allows users to create accounts, securely log in, and manage their personal tasks through a simple and responsive interface.


- **Name:** Mohamed Mahmoud
- **ID:** 2304096
- **Contribution:** Database design, Flask backend, user authentication, and To-Do list functionality.

## ✨ Features

- **User Registration:** Create a new account using a name, email, and password.
- **User Login:** Authenticate users using their email and password.
- **Password Security:** Store passwords as bcrypt hashes instead of plain text.
- **Personal To-Do List:** Each user can access their own tasks.
- **Add Tasks:** Create new tasks with title validation.
- **Edit Tasks:** Update existing task titles.
- **Mark Tasks as Done:** Change tasks between completed and pending.
- **Delete Tasks:** Remove tasks when they are no longer needed.
- **Input Validation:** Validate registration, login, and task forms on both the client and server sides.
- **Protected Pages:** Require authentication to access the To-Do list and task management routes.
- **Dark Mode:** Switch between light and dark themes.
- **Responsive Design:** Adapt the interface to different screen sizes.
- **Database Integration:** Store user accounts and tasks in MySQL.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web framework and backend routing |
| MySQL | Relational database |
| PyMySQL | Connect Python to MySQL |
| bcrypt | Password hashing |
| HTML5 | Page structure |
| CSS3 | Styling and responsive layout |
| JavaScript | Client-side form validation and dark mode |
| python-dotenv | Load configuration from environment variables |

## 🗄️ Database Design

The application uses a MySQL database named `registration` with two tables.

### 1. Users Table

Stores registered user information.

| Column | Description |
|---|---|
| `user_id` | Primary key; automatically generated |
| `email` | Unique user email |
| `name` | User's name |
| `password_hash` | Bcrypt password hash |
| `registration_date` | Account creation timestamp |

### 2. To-Dos Table

Stores tasks belonging to registered users.

| Column | Description |
|---|---|
| `todo_id` | Primary key; automatically generated |
| `user_id` | Foreign key referencing `users.user_id` |
| `title` | Task title |
| `is_done` | Task completion status |
| `created_at` | Task creation timestamp |

**Relationship:** One user can have multiple tasks. The `user_id` foreign key connects each task to its owner.

## 📸## 4. Screenshots

## 1. User Registration

![User Registration](Screenshot%202026-10-12%20112610.png)

Users can create an account by entering their name, email, password, and password confirmation.

## 2. Login Page

![Login Page](Screenshot%202026-10-12%20112958.png)

Registered users can log in using their email and password.

## 3. Add New Task

![My To-Do List](Screenshot%202026-10-12%20113525.png)

Users can view their tasks, edit task titles, mark tasks as completed, and delete tasks.

## 4. My To-Do List

![Add New Task](Screenshot%202026-10-12%20125722.png)

Users can add new tasks to their personal to-do list.

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have installed:

- Python 3
- MySQL Server
- Git (optional)

### Step 1: Clone the Repository

```bash
git clone https://github.com/rewansrour123/My_Todo_list.git
cd My_Todo_list
```

Alternatively, download the repository and open its folder in your terminal.

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory using `.env.example` as a template.

Example configuration:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=registration
DB_PORT=3306
SECRET_KEY=replace_with_a_random_secret_key
```

Replace `your_mysql_password` with your actual MySQL password and use a secure, randomly generated secret key.

**Security note:** Never upload your real `.env` file or database credentials to GitHub.

### Step 5: Create the Database

Open MySQL Workbench or your MySQL terminal and execute the following SQL script:

```sql
DROP DATABASE IF EXISTS registration;

CREATE DATABASE registration;

USE registration;

CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id),
    UNIQUE (email)
);

CREATE TABLE todos (
    todo_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    is_done TINYINT(1) NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (todo_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

**Important:** The script drops the existing `registration` database before recreating it. Back up any important data before executing it.

### Step 6: Run the Application

From the project root directory, run:

```bash
python app.py
```

Open the following address in your browser:

http://127.0.0.1:5000/

New visitors are redirected to the registration page. After registration or login, users can access their personal To-Do list.

## 🔐 Security and Validation

- Passwords are hashed using bcrypt before being stored in the database.
- Parameterized SQL queries are used to reduce SQL injection risks.
- Protected routes require a logged-in session.
- Task update and deletion queries check that the task belongs to the logged-in user.
- Form inputs are validated in JavaScript and Flask.
- Environment variables are used for database settings and the Flask secret key.

## 📂 Project Structure

```text
My_Todo_list/
├── app.py                 # Flask application and routes
├── db.py                  # MySQL connection
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore              # Excluded files
├── README.md               # Project documentation
├── templates/
│   ├── register.html       # Registration page
│   ├── login.html          # Login page
│   ├── todos.html          # Personal task list
│   └── add_todo.html       # Add task page
├── static/
│   ├── style.css           # Application styling
│   └── validation.js       # Client-side validation
└── screenshots/            # Application screenshots
```

## 🎯 Learning Objectives

This project demonstrates the practical application of:

- Relational database design and SQL table creation.
- Primary keys, foreign keys, and unique constraints.
- Connecting a Flask application to a MySQL database.
- Implementing user registration, login, and session management.
- Performing CRUD operations: Create, Read, Update, and Delete.
- Validating user input and handling errors.
- Building a responsive web interface.

## 👨‍💻 Author

**Mohamed Mahmoud**  
Introduction to Database Systems — Lab 2  
Faculty of Engineering, Alexandria National University

---

*Developed for educational purposes as part of the Fall 2026 Database Systems Lab.*
