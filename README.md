# Mini Blog Project (Interview Assessment)

This repository contains a **mini blog web application** developed as part of an interview assessment.

##  Project Overview

The application allows users to:
- Register and log in securely
- Create blog posts with image uploads
- Upload Excel files and display their rows and columns on the website
- Upload and manage files through the web interface

The project was built following the given requirements and tech stack.

---

##  Tech Stack

- **Backend:** Django
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Libraries:** jQuery

---

##  Features

###  User Authentication & Authorization
- User registration
- Login & logout
- Access control for authenticated users

###  Blog Posts
- Create blog posts
- Upload and display images with posts

###  Excel File Upload
- Upload Excel files (`.xls`, `.xlsx`)
- Display rows and columns dynamically on the website

###  File Upload
- Upload files through the web interface
- Server-side handling using Django

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/realTNEU/mini-blog.git
cd mini-blog
```
### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database

-->Create a MySQL database
-->Update database credentials in settings.py

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Start the Server
```bash
python manage.py runserver
```
### Access the app
http://127.0.0.1:8000


## 👤 Author

**Ameya Taneja**  
GitHub: https://github.com/realTNEU

