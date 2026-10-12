# Lab 2: Login & To-Do Application

## 1. Team Members

- Name: Mohamed Mahmoud
- ID: [2304096]
- Contributions: Database design, Flask backend, authentication, and to-do list.

## 2. Technologies Used

- Backend: Python and Flask
- Frontend: HTML, CSS, and JavaScript
- Database: MySQL
- Database connection: PyMySQL
- Password hashing: bcrypt

## 3. How to Run the Project

1. Install Python and MySQL.
2. Install the required Python packages:

   `pip install -r requirements.txt`

3. Run `database/schema.sql` in MySQL to create the database and tables.
4. Copy `.env.example` to `.env`.
5. Set the correct MySQL password and a random secret key in `.env`.
6. Start the Flask application:

   `python app.py`

7. Open `http://127.0.0.1:5000/register` in your browser.

## 4. Implemented Features

- R1: User registration and duplicate email handling.
- R2: Login, password verification, and logout.
- R3: Private to-do list using sessions.
- R4: Add a to-do.
- R5: Edit a to-do title.
- R6: Mark a to-do as done or not done.
- R7: Delete a to-do with confirmation.
- R8: Browser and server-side input validation.
- R9: bcrypt password hashing and parameterized SQL queries.
- R10: Responsive interface using CSS.

## 5. Screenshots

Add screenshots of:

1. Registration page with validation errors.
2. Login page.
3. To-do list containing at least one completed task.
4. The website displayed in a phone-sized window.

## 6. Database Questions

### (a) Why do UPDATE and DELETE contain AND user_id = ?

This condition ensures that a user can only modify or delete their own tasks. Without it, a user might modify or delete another user's task by providing its ID.

### (b) What happens if a to-do references a nonexistent user_id?

MySQL rejects the insert because of the foreign key constraint. This preserves referential integrity.

### (c) Why store a password hash instead of the password?

A password hash prevents the application from storing passwords in plaintext. bcrypt also uses a salt and is intentionally slow, making password guessing more difficult.

### (d) Why check an empty name when the column is NOT NULL?

NOT NULL prevents SQL NULL values, but it allows empty strings and strings containing only spaces. Application validation is needed to reject those values.
