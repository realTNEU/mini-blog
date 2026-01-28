# Mini Blog - Django Web Application

## 🚀 Features

✅ **User Authentication**
- Secure registration and login system
- Password validation
- Session management

✅ **Blog Posts**
- Create and view blog posts
- All users can view posts
- Only authenticated users can create posts
- Author and timestamp tracking

✅ **File Upload System**
- Upload various file types (Excel, CSV, PDF, Images, etc.)
- Automatic file type detection
- File size calculation
- **Excel/CSV Analysis**: Automatically detects rows and columns
- File listing with detailed metadata

## 🛠️ Tech Stack

- **Backend**: Python 3.12 + Django 5.1.5
- **Database**: MySQL 8.0
- **Frontend**: HTML5, Bootstrap 5.3, jQuery 3.7
- **File Processing**: Pandas, OpenPyXL
- **Environment**: Python dotenv

## 📁 Project Structure

```
mini-blog/
├── accounts/         # User authentication app
├── posts/           # Blog posts app  
├── files/           # File upload app
├── config/          # Django settings
├── templates/       # HTML templates
├── static/          # CSS, JS files
├── media/           # User uploads
└── venv/            # Virtual environment
```

## 🔧 Setup Instructions

### 1. Database Setup
```bash
# MySQL database and user already created:
# Database: <db>
# User: <user>
# Password: <password>
```

### 2. Environment Variables
The `.env` file contains:
```
SECRET_KEY=scikiq-task
DEBUG=True
DB_NAME=<db>
DB_USER=<user>
DB_PASSWORD=<password>
DB_HOST=localhost
```

### 3. Install Dependencies
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User
```bash
python manage.py createsuperuser
# Username: admin
# Password: admin123 (already set)
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

## 📝 Usage

### For Users:
1. **Register** an account at `/accounts/register/`
2. **Login** at `/accounts/login/`
3. **View all posts** at `/posts/`
4. **Create posts** at `/posts/create/`
5. **Upload files** at `/files/upload/`
6. **View files** at `/files/`

### For Admins:
- Admin panel: http://127.0.0.1:8000/admin/
- Username: `admin`
- Password: `admin123`

## 🎨 Frontend Features

- **Responsive Design**: Bootstrap 5.3
- **Interactive UI**: jQuery for dynamic interactions
- **Icons**: Bootstrap Icons
- **Animations**: Hover effects and transitions
- **Real-time Updates**: Character counter, file preview

## 📊 File Upload Features

When you upload a file:
- **File Name**: Original filename preserved
- **File Type**: Auto-detected (Excel, CSV, PDF, Image, Other)
- **File Size**: Displayed in human-readable format
- **Upload Date**: Timestamp recorded
- **Uploader**: Linked to user account
- **Excel/CSV**: Shows row and column count automatically!

## 🔒 Security Features

- CSRF protection enabled
- Password validation
- Secure session management
- Login required decorators
- Environment variables for sensitive data

## 📦 Models

### User (accounts/models.py)
- Extends Django's AbstractUser
- Custom user model

### Post (posts/models.py)
- Title, Content
- Author (ForeignKey to User)
- Timestamps (created_at, updated_at)

### UploadedFile (files/models.py)
- File upload
- File metadata (name, type, size)
- Excel analysis (rows, columns)
- Uploader tracking

## 🎓 Learning Outcomes

As a student, you learned:
1. Django project setup and configuration
2. MySQL database integration
3. Custom user authentication
4. Model-View-Template (MVT) pattern
5. Form handling and file uploads
6. Bootstrap and jQuery integration
7. Git version control
8. Environment variable management
9. File processing with Pandas

## 📌 Git Repository

All changes committed to the repository.

---

**Developer**: Ameya
**Date**: January 21, 2026
**Version**: 1.0.0
