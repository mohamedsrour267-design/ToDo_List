# Login & To-Do Application

A web-based **Login and To-Do Management System** developed using Flask and MySQL for Lab 2 of the Introduction to Database Systems course at Alexandria National University.

The application provides secure user authentication and allows each user to manage their own personal tasks through a simple, responsive interface.

---

## 👥 1. Team Members

| Name | Student ID | Contributions |
|---|---|---|
| Rewan Mahmoud Mohamed | 2304098 | Database Design, Flask Backend, Authentication, and To-Do List |

---

## 🛠️ 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Client-side interactions and theme switching |
| MySQL | Database management |
| PyMySQL | Connecting Python to MySQL |
| bcrypt | Password hashing |
| Flask Sessions | User authentication state |
| python-dotenv | Environment variable configuration |
| Git & GitHub | Version control and project hosting |

---

## ✨ 3. Implemented Features

- **User Registration:** Create a new account with input validation.
- **Login & Logout:** Authenticate users and manage their sessions.
- **Duplicate Email Handling:** Prevent registration with an already registered email.
- **Password Security:** Hash passwords using bcrypt instead of storing them in plaintext.
- **Protected Pages:** Restrict access to authenticated users.
- **Personal To-Do Lists:** Keep each user's tasks associated with their account.
- **Add Tasks:** Create new to-do items.
- **Edit Tasks:** Update existing task titles.
- **Task Completion:** Mark tasks as completed or incomplete.
- **Delete Tasks:** Remove tasks with confirmation.
- **Input Validation:** Validate user input on both the client and server sides.
- **Task Title Limit:** Restrict task titles to a maximum of 200 characters.
- **SQL Injection Protection:** Use parameterized SQL queries.
- **Responsive Design:** Support different screen sizes.
- **Dark Mode & Light Mode:** Switch between visual themes.

---

## 📁 4. Project Structure

```text
My_Todo_list/
│
├── app.py
├── schema.sql
├── env.example
├── .gitignore
├── README.md
│
├── login.html
├── register.html
├── todos.html
│
├── style.css
├── theme.js
│
├── Screenshot 2026-10-12 121621.png
├── Screenshot 2026-10-12 121837.png
├── Screenshot 2026-10-12 121945.png
└── Screenshot 2026-10-12 122026.png
```

---

## 🚀 5. Installation & Setup

### Prerequisites

Make sure the following software is installed:

- Python
- MySQL Server
- MySQL Workbench or another MySQL client

### Step 1: Clone the Repository

```bash
git clone https://github.com/rewansrour123/My_Todo_list.git
cd My_Todo_list
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install flask pymysql bcrypt python-dotenv
```

### Step 3: Set Up the Database

1. Open MySQL Workbench.
2. Open the `schema.sql` file from the project directory.
3. Execute the SQL script to create the database and tables.

### Step 4: Configure Environment Variables

1. Create a copy of `env.example`.
2. Rename the copy to `.env`.
3. Enter your local MySQL credentials and a strong, randomly generated Flask secret key.

**Security note:** Never commit your actual `.env` file, database password, or secret key to GitHub.

### Step 5: Run the Application

Start the Flask application from the project directory:

```bash
python app.py
```

### Step 6: Open the Website

Open the registration page in your browser:

**http://127.0.0.1:5000/register**

Create an account, log in, and start managing your tasks.

---

## 📸 6. Application Screenshots

### 1. Registration Page

The registration page allows new users to create accounts and displays validation feedback when applicable.

![Registration Page](Screenshot%202026-10-12%20121621.png)

### 2. To-Do List Management

The main task management page allows authenticated users to add, edit, complete, and delete their personal tasks.

![To-Do List Management](Screenshot%202026-10-12%20121945.png)

### 3. Login Page

The login page allows existing users to access their accounts.

![Login Page](Screenshot%202026-10-12%20121837.png)

### 4. Responsive Design

The responsive layout demonstrates how the application appears in a phone-sized browser viewport.

![Responsive Design](Screenshot%202026-10-12%20122026.png)

---

## 🗄️ 7. Database & Security Questions

### (a) Why do UPDATE and DELETE queries contain `AND user_id = %s`?

This condition ensures that users can modify or delete only their own tasks. Without it, a user might access another user's task by supplying its ID. Including the user ID in the query adds an important authorization check.

### (b) What happens if a to-do references a nonexistent `user_id`?

If a foreign key constraint is defined and enforced, MySQL rejects the operation because the referenced user does not exist. This preserves referential integrity between the users and todos tables.

### (c) Why store a password hash instead of the original password?

Storing a password hash prevents the application from keeping passwords in plaintext. bcrypt uses a salt and a computationally expensive hashing process, making password-guessing attacks more difficult.

### (d) Why validate an empty name when the database column is `NOT NULL`?

The `NOT NULL` constraint prevents NULL values, but it does not necessarily prevent empty strings or strings containing only spaces. Application-level validation is required to reject these inputs.

### (e) Why use both client-side and server-side validation?

Client-side validation provides immediate feedback and improves the user experience. Server-side validation is essential because browser checks can be bypassed and requests can be sent directly to the backend.

### (f) Why use parameterized SQL queries?

Parameterized SQL queries separate SQL commands from user-provided values, helping prevent SQL injection attacks.

---

## 🔐 8. Security Considerations

The project applies several basic security practices:

- Password hashing with bcrypt.
- Session-based authentication.
- User-specific task ownership checks.
- Parameterized database queries.
- Server-side input validation.
- Environment variables for sensitive configuration.

These practices help protect user accounts and task data. Production deployment would require additional security configuration and testing.

---

## 🎓 9. Course Information

- **University:** Alexandria National University
- **Faculty:** Faculty of Engineering
- **Course:** Introduction to Database Systems
- **Lab:** Lab 2 — Login & To-Do Application
- **Semester:** Fall 2026

---

## 👩‍💻 Author

**Rewan Mahmoud Mohamed**

GitHub: [@rewansrour123](https://github.com/rewansrour123)

---

*Developed as part of the Introduction to Database Systems course — Fall 2026.*
