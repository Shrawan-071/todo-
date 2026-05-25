# 📝 Flask To-Do App

A simple and responsive To-Do web application built using **Flask**, **SQLite**, and **SQLAlchemy**.  
This project allows users to create, update, delete, and manage tasks easily through a web interface.

---

## 🚀 Live Demo
https://todo-rust-chi.vercel.app/
---

## ⚙️ Features

- ➕ Add new tasks
- 📝 Update existing tasks
- ❌ Delete tasks
- 📋 View all tasks in a table
- 📌 Track task status (Pending / Done)
- 💾 SQLite database integration
- 🎨 Clean and simple UI using HTML & CSS

---

## 🛠️ Tech Stack

- Backend: Flask (Python)
- Database: SQLite (SQLAlchemy ORM)
- Frontend: HTML, CSS
- Deployment: Vercel (Serverless)

---

## 📁 Project Structure

project/
│── app.py
│── vercel.json
│── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── update.html
│
└── static/
    └── style.css

---

## ⚡ Installation & Setup (Local)

### 1. Clone the repository
git clone https://github.com/your-username/todo-flask-app.git
cd todo-flask-app

---

### 2. Create virtual environment
python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3. Install dependencies
pip install -r requirements.txt

---

### 4. Run the app
python app.py

Open:
http://127.0.0.1:5000/

---

## 🌐 Deployment (Vercel)

1. Push project to GitHub  
2. Import repository in Vercel  
3. Ensure:
   - app.py is entry point
   - vercel.json is configured properly  
4. Click Deploy  

---

## ⚠️ Important Notes

- SQLite database runs in `/tmp` on Vercel
- Data resets after redeployment
- Best for demo projects, not production apps

---

## 👨‍💻 Author

- Name: Shrawan Gupta  
- Role: AI Engineer & Full Stack Developer  
- Skills: Python, Flask, SQL, HTML, CSS, JavaScript  

---

## 📌 Future Improvements

- User authentication (login/register)
- Cloud database (PostgreSQL / MongoDB)
- REST API version
- React frontend upgrade
- Better UI/UX improvements

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub.
