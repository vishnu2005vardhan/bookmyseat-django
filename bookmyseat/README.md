# 📚 BookMySeat – Django CRUD Web Application

BookMySeat is a **Django-based full stack web application** built to understand and implement **core Django concepts**, authentication, database operations, and frontend integration using Bootstrap.

This project is suitable for:
- College mini project
- Django learning
- Full Stack Developer preparation
- GitHub portfolio showcase

---

## 🔥 Features

### 🔐 Authentication
- User Signup
- User Login
- User Logout
- Session-based authentication
- Protected routes using `@login_required`

### 🧑‍🎓 Student Management (CRUD)
- Add Student
- View Student List
- Edit Student Details
- Delete Student
- Each student is linked to the logged-in user

### 🎨 UI
- Bootstrap 5 styling
- Reusable base template
- Simple and clean dashboard

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, Bootstrap 5  
- **Database:** SQLite  
- **Version Control:** Git, GitHub  

---

## 📁 Project Structure

bookmyseat/
│
├── bookmyseat/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── mainapp/
│ ├── migrations/
│ ├── templates/
│ │ └── mainapp/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── signup.html
│ │ ├── student_list.html
│ │ ├── add_student.html
│ │ └── edit_student.html
│ ├── models.py
│ ├── views.py
│ └── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md


---

## 🧠 Database Model

### Student Model

| Field  | Type |
|------|------|
| name | CharField |
| age | IntegerField |
| course | CharField |
| user | ForeignKey (Django User) |

Each student record is associated with a **specific logged-in user**.

---

## ⚙️ How to Run the Project

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/bookmyseat.git
cd bookmyseat

###Create Virtual Environment(OPtional)
python -m venv venv
venv\Scripts\activate

###Install Django
pip install django

###Apply Migrations
python manage.py makemigrations
python manage.py migrate

###Create Superuser(Optional)
python manage.py createsuperuser

###Run Server
python manage.py runserver



👨‍💻### Author

Vishnu Vardhan Reddy
Aspiring Software Developer
Bengaluru

