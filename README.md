🎯 Quiz Platform — Project Documentation
📌 Overview

This document describes the design and functionality of a web-based quiz platform.
The application allows users to complete quizzes, earn points 🏆, unlock advanced challenges 🔓, and compete on a global leaderboard 🌍.


🎯 Project Goals
The purpose of the project is to demonstrate the development of a modern web application using Django and PostgreSQL, with focus on:

- 👤 secure user authentication and profiles
- 🧠 quiz creation and management
- ⭐ scoring, progress, and achievements
- ⚡ fast and interactive user experience

🧩 Core Features
The platform includes:

- 🔐 User registration and login
- 🖼️ Editable user profiles (avatar, name, email, stats)
- 📝 Quiz system with basic and advanced levels
- 🔓 Unlocking logic — advanced quizzes require completion of earlier ones
- 🏆 Points, titles, and global ranking
- 🛠️ Admin panel for creating quizzes and questions
- 🔎 Dynamic search for quizzes

🛠️ Technology Stack

- 🐍 Backend: Django (Python)
- 🗄️ Database: PostgreSQL
- 🌐 Frontend: HTML, CSS, JavaScript (AJAX)

The system is designed to be modular, scalable, and easy to extend — new quizzes, achievements, and features can be added without major changes.

# **Contents**

 1. Technologies used to create the site
 2. Main components and their implementation
  - 2.1 Registration form
  - 2.2 Login form
  - 2.3 User profile
  - 2.4 Logic for unlocking the advanced quiz
  - 2.5 Creating tests and questions
 3. Dynamic search
 
# **1. Technologies used to create the site**

The site is built with Django — a Python web framework that provides ready-made components for working with forms, users, databases, and templates.
The front-end part uses HTML, CSS, and JavaScript (AJAX for dynamic communication).

<img width="1531" height="744" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/a758dd3f-8416-4d93-89a4-f3b53d5e8a4c" />

<img width="1160" height="805" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/a339e23c-7fe6-410a-96f4-ca1f80d09d9b" />

# **2.1 Registration form**

The registration form is created manually using Django forms.
It validates whether the username and email already exist in the database.
An example view is shown in Figure 1.

<img width="497" height="611" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/806be30b-f3ed-47d9-8f4b-a5b2483f38c7" />

# **2.2 Login form**

The login form uses Django’s built-in AuthenticationForm, which processes the username and password.
Figure 2 shows the login form.

During registration, a check is performed to see whether the username or email already exists in the database.

<img width="736" height="510" alt="Screenshot (16)" src="https://github.com/user-attachments/assets/c03241c0-ca37-4ca0-a0bd-f8f552be2544" />

<img width="864" height="797" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/b1de25ee-328c-43d6-aa18-f5cf2971f9e8" />

# **2.3 User profile**

The profile page contains:

- photo
- name
- email
- completed quizzes
- ranking

The user can edit their information using the “Edit profile” button.

The “Edit profile” button uses a form, view, and template in Django.

<img width="810" height="798" alt="Screenshot (18)" src="https://github.com/user-attachments/assets/0193f048-0291-4415-9795-02e627091127" />

# **2.4 Logic for unlocking the advanced quiz**

The advanced quiz can only be accessed if the user has completed the basic quiz.
The check is performed through a Django view that tracks the user’s score and progress.

Answers can be typed in lowercase or uppercase (case-insensitive), because they are converted during validation.

Validation happens through a view + AJAX (JavaScript) for a better user experience.

The user can complete the quiz only if they answer all questions correctly.

After completing the basic quiz, the advanced one is unlocked.

<img width="1121" height="529" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/1bf400e3-44db-4621-bf81-2e59a82974a7" />


<img width="1113" height="481" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/846c57af-203d-4ad9-868e-9586a80c211c" />

<img width="1107" height="515" alt="Screenshot (25)" src="https://github.com/user-attachments/assets/aaadcd39-9a11-4d77-bf07-02cd42d6fe5c" />

# **2.5 Creating tests and questions**

Quizzes are created through Django admin.
The administrator defines:

the basic structure of the tests

quiz types (basic and advanced)

the correct answers

Figure 3 — Administrator panel for creating quizzes.

# **3. Dynamic search**
The search feature is implemented using a Django form and an AJAX request, which allows filtering results without reloading the page.

<img width="1384" height="559" alt="Screenshot (26)" src="https://github.com/user-attachments/assets/c8c81fd8-9ef7-4d0f-a27d-30afce71c485" />


# **Conclusion**

In this project, I developed a quiz website using the Django framework, combined with HTML, CSS, and JavaScript (AJAX). The platform allows users to register, log in, manage their profile, complete quizzes, and unlock advanced quizzes after successfully finishing the basic ones. The idea and structure were partly inspired by platforms such as TryHackMe, where learning is organized through progressive tasks and challenges. This project demonstrates how Django simplifies authentication, form handling, and database operations while still supporting dynamic, interactive functionality.
In the future, the project could be extended with additional quiz categories, time-limited challenges, more detailed statistics, achievements/badges, and better mobile optimization. These improvements would make the site more engaging and bring it closer to real educational and training platforms.

