# Quick Start Guide - Mini Blog

## 🟢 Server is Running!

Your Django development server is running at: **http://127.0.0.1:8000/**

## 🔐 Login Credentials

### Admin Panel (http://127.0.0.1:8000/admin/)
- Username: `admin`  
- Password: `admin123`

## 📍 Important URLs

| Page | URL | Description |
|------|-----|-------------|
| Home | http://127.0.0.1:8000/ | Redirects to posts |
| All Posts | http://127.0.0.1:8000/posts/ | View all blog posts |
| Create Post | http://127.0.0.1:8000/posts/create/ | Create new post (login required) |
| All Files | http://127.0.0.1:8000/files/ | View uploaded files |
| Upload File | http://127.0.0.1:8000/files/upload/ | Upload files (login required) |
| Login | http://127.0.0.1:8000/accounts/login/ | User login |
| Register | http://127.0.0.1:8000/accounts/register/ | New user registration |
| Admin | http://127.0.0.1:8000/admin/ | Django admin panel |

## ✅ What's Been Completed

1. ✓ MySQL database created and configured
2. ✓ Django project structure set up
3. ✓ Custom user authentication system
4. ✓ Blog posts app with create/view functionality
5. ✓ File upload system with Excel analysis
6. ✓ Beautiful frontend with Bootstrap & jQuery
7. ✓ All templates created
8. ✓ Git repository initialized and commits made

## 🎯 Try These Features

### 1. Create Your First User
1. Go to: http://127.0.0.1:8000/accounts/register/
2. Fill in username, email, password
3. You'll be auto-logged in!

### 2. Create a Blog Post
1. Login
2. Click "New Post" in navbar
3. Enter title and content
4. Click "Publish Post"

### 3. Upload a File
1. Login  
2. Click "Upload" in navbar
3. Choose any file (try an Excel file!)
4. See automatic analysis (rows/columns for Excel/CSV)

### 4. Test Excel Analysis
Create a test Excel file:
```bash
cd /home/ameya/Projects/mini-blog
python << EOF
import pandas as pd
df = pd.DataFrame({'Name': ['John', 'Jane', 'Bob'], 'Age': [25, 30, 35]})
df.to_excel('test.xlsx', index=False)
print('✓ test.xlsx created with 3 rows and 2 columns')
EOF
```

Then upload `test.xlsx` and watch it detect 3 rows, 2 columns!

## 🛠️ Useful Commands

### Start Server
```bash
cd /home/ameya/Projects/mini-blog
source venv/bin/activate
python manage.py runserver
```

### Stop Server
Press `Ctrl+C` in terminal

### Create Superuser
```bash
python manage.py createsuperuser
```

### Make Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Access MySQL Database
```bash
mysql -u bloguser -p'BlogMaster123@' miniblog
```

### Django Shell
```bash
python manage.py shell
```

## 📚 Next Steps to Learn

1. **Add Edit/Delete Posts**: Add views to edit and delete posts
2. **User Profiles**: Create profile pages for users
3. **Comments**: Add commenting system to posts
4. **Search**: Implement search functionality
5. **Pagination**: Add pagination to posts list
6. **File Download**: Add download button for files
7. **Image Preview**: Show image thumbnails in file list
8. **Rich Text Editor**: Add WYSIWYG editor for posts
9. **Categories/Tags**: Organize posts with categories
10. **Email Notifications**: Send emails on new posts

## 🐛 Troubleshooting

### Server won't start?
```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill process if needed
kill -9 <PID>
```

### Database connection error?
```bash
# Check MySQL is running
sudo systemctl status mysql

# Test connection
mysql -u bloguser -p'BlogMaster123@' miniblog
```

### Static files not loading?
```bash
python manage.py collectstatic
```

## 📖 Project File Overview

- `manage.py` - Django management script
- `config/settings.py` - Project settings
- `config/urls.py` - URL routing
- `.env` - Environment variables
- `requirements.txt` - Python dependencies
- `db.sqlite3` - SQLite database (not used, we use MySQL)

## 💡 Tips

- Always activate virtual environment before running commands
- Use admin panel to manage data easily
- Check browser console for JavaScript errors
- Use Django debug toolbar for development (optional)
- Git commit frequently!

---

**Have fun building your mini blog! 🚀**
