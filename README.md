# 🩸 BloodCare – Blood Donor Management System

BloodCare is a simple web-based Blood Donor Management System developed using Python Flask and SQLite. It helps users find blood donors and allows administrators to manage donor records.

## ✨ Features

- Donor Registration
- Search Donors by Blood Group and City
- View Registered Donors
- Admin Login System
- Admin Dashboard
- Edit Donor Details
- Delete Donor Records
- Total Registered Donors Counter
- Responsive Design for Mobile and Desktop

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Database:** SQLite
- **Code Editor:** Visual Studio Code

## 📁 Project Structure

```text
Blood_Donor_Management_System/
│
├── app.py
├── database.py
├── donors.db
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── donors.html
│   ├── admin_login.html
│   ├── admin.html
│   └── edit_donor.html
│
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mowaisr/Blood-Donor-Management-System.git
```

### 2. Open the Project Folder

```bash
cd Blood-Donor-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Flask

```bash
pip install Flask
```

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000/

## 🔐 Admin Panel

The project includes an admin login system to manage donor records.

Admin credentials are configured in the application. Contact the project owner for access.

## 🎯 Project Objective

The main objective of BloodCare is to make it easier to connect blood donors with people who need blood and to simplify donor record management.

## 👨‍💻 Author

**Mohammad Owais Raza**

GitHub: [@mowaisr](https://github.com/mowaisr)

---

*Made with ❤️ to support blood donation and save lives.*