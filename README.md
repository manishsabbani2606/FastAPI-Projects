**# 🚀 Product Management Tracker

A full-stack Product Management application built using **FastAPI (Backend)** and **React (Frontend)**.  
This application allows users to manage products with full CRUD functionality integrated with PostgreSQL.

---

## 🛠 Tech Stack

### 🔹 Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

### 🔹 Frontend
- React (Create React App)
- Axios
- CSS

---

## 📌 Features

- Create new products
- View all products
- View product by ID
- Update product details
- Delete products
- PostgreSQL database integration
- RESTful API design
- Interactive API docs via Swagger

---

## 📂 Project Structure

│
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── database_models.py
│ ├── models.py
│ └── requirements.txt
│
├── frontend/
│ ├── public/
│ ├── src/
│ ├── package.json
│ └── package-lock.json
│
└── README.md



---

## ⚙️ Backend Setup (FastAPI)

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux


2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Database

Update database.py with your PostgreSQL credentials:

DATABASE_URL = "postgresql://username:password@localhost:5432/dbname"


If password contains special characters, URL encode it.

4️⃣ Run Server
uvicorn main:app --reload


API available at:

http://127.0.0.1:8000


Swagger Docs:

http://127.0.0.1:8000/docs

💻 Frontend Setup (React)
1️⃣ Navigate to frontend folder
cd frontend

2️⃣ Install Dependencies
npm install

3️⃣ Start React App
npm start


App runs at:

http://localhost:3000

🔌 API Endpoints
Method	Endpoint	Description
GET	/products	Get all products
GET	/products/{id}	Get product by ID
POST	/products	Create product
PUT	/products/{id}	Update product
DELETE	/products/{id}	Delete product
📊 Sample Product JSON
{
  "name": "Laptop",
  "description": "High performance laptop",
  "price": 999.99,
  "quantity": 10
}

🧠 Architecture Overview

Frontend (React)
⬇ Axios HTTP Requests
Backend (FastAPI REST API)
⬇ SQLAlchemy ORM
PostgreSQL Database

🔒 Future Improvements

Authentication (JWT)

User management

Role-based access control

Dockerization

Cloud deployment (AWS / Render / Railway)

CI/CD pipeline integration

📌 Author

Manish Sabbani
Full-Stack Developer | Data & Cloud Engineer

⭐ If You Like This Project

Give it a star ⭐ on GitHub!


---

# 🚀 Optional (More Professional Touch)

If this is for portfolio, I can also give you:

- 🔥 Advanced README with badges
- 🐳 Docker version
- ☁ Deployment guide (Render / AWS)
- 📸 Screenshot section template
- 🧱 Enterprise folder restructuring

Just tell me what level you want — student, mid-level, or production-ready 🚀**
