# 🏢 HR ERP Management System

<p align="left">
 <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
 <img src="https://img.shields.io/badge/Flask-2.x-green?logo=flask&logoColor=white" alt="Flask">
 <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
 <img src="https://img.shields.io/badge/Deployed-Vercel-black?logo=vercel&logoColor=white" alt="Vercel">
 <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

A full-stack **HR ERP web application** built with Flask that streamlines employee management — from onboarding new hires to searching, updating, and maintaining employee records through a secure admin dashboard.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Admin Authentication** | Session-based admin login with protected routes |
| 👤 **Add Employees** | Register new employees with name, email, mobile, designation & salary |
| 📋 **View Employees** | Table view of all employee records in the dashboard |
| 🔍 **Search Employees** | Instant search employees by name |
| ✏️ **Update Records** | Edit and update existing employee details |
| 🗑️ **Delete Records** | Remove employees from the system |
| 🛡️ **Access Control** | Every admin route is guarded by an auth check |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite with Flask-SQLAlchemy ORM
- **Frontend:** HTML5, CSS3, Jinja2 Templates
- **Authentication:** Flask Session Management
- **Deployment:** Vercel (Serverless)

---

## 📁 Project Structure

```
HR-ERP-System/
│
├── api/
│   └── index.py            # Vercel serverless entry point
├── app.py                  # Main Flask application (routes, models, config)
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel deployment configuration
│
├── templates/
│   ├── header.html
│   ├── adminheader.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── adminlogin.html
│   ├── admindas.html
│   ├── addemploy.html
│   ├── showemploy.html
│   ├── searchemploy.html
│   ├── profile.html
│   ├── update.html
│   ├── delete.html
│   └── admin_registration_succes.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/narendrakp222/hr-erp-system.git
   cd hr-erp-system
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   ```

   ```bash
   # Windows (PowerShell)
   .\env\Scripts\activate

   # macOS / Linux
   source env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. Open your browser and visit → **http://127.0.0.1:5000/**

### 🔑 Default Admin Credentials

| Username | Password |
|---|---|
| `admin` | `super` |

---

## 🌐 Deployment (Vercel)

The project is configured for one-click deployment on Vercel:

1. Push this repository to GitHub
2. Import the repo on [Vercel](https://vercel.com/new)
3. Vercel auto-detects the Python runtime and deploys using `api/index.py` and `vercel.json`

> **Note:** SQLite is ephemeral on serverless platforms. For production use, connect a persistent database (e.g., Vercel Postgres, Neon, or Supabase).

---

## 📸 Screenshots

> Add screenshots of the landing page, admin dashboard, and employee list here to make the README even better.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)

---

## 👨‍💻 Author

**Narendra Paswan** — [GitHub](https://github.com/narendrakp222)

---

## 📄 License

This project is licensed under the MIT License.
