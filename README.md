## Financial Project

A Django REST API application for managing financial transactions and accounts, deployed on **Heroku**.

---

## 📌 Project Overview

This project provides an API for creating and managing financial accounts and transactions.  
It supports **role-based access control** with three user groups:

- **Admin** – Full access (read/write)  
- **Financial Analyst** – Full access (read/write)  
- **Auditor** – Read-only access  

The API uses **Token Authentication** for secure access.

---

## 🚀 Features

- CRUD operations for **Accounts** and **Transactions**  
- Role-based permissions  
- Token-based authentication with Django REST Framework  
- Deployed on Heroku with **PostgreSQL backend (Amazon RDS)**  
- **CORS enabled** for frontend integration  

---

## ⚙️ Setup and Installation

### Prerequisites
- Python **3.9+**
- pip
- Git
- Heroku CLI (for deployment)
- PostgreSQL (optional for local development)

---

### 🔧 Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd financial_project
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables** (e.g., in `.env`)
   ```env
   DJANGO_SECRET_KEY=your-secret-key
   DATABASE_URL=your_local_or_heroku_database_url
   DEBUG=True
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## ☁️ Deployment on Heroku

The app is deployed at:  
🔗 https://transactionsapp-b3316d905d81.herokuapp.com/

**Environment variables on Heroku include:**
- `DATABASE_URL`
- `DJANGO_SECRET_KEY`
- `DEBUG` (set to `False`)

**Deployment commands:**
```bash
heroku login
heroku git:remote -a transactionsapp
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

---

## 🏗️ Architecture & Design

### Apps and Models
- `transactions` app contains two main models:
  - **Account**
  - **Transaction**

### Authentication & Permissions
- Uses **Django REST Framework's TokenAuthentication**
- Custom permission classes:
  - `IsAdminOrReadOnly`
  - `IsFinancialAnalystOrReadOnly`
  - `IsAuditorReadOnly`
- Users belong to groups that determine their permissions

---

## 📡 API Endpoints

| Endpoint               | Method | Description                  | Authentication | Permissions |
|-------------------------|--------|------------------------------|----------------|-------------|
| `/accounts/`            | GET    | List all accounts            | Required       | Admin, Financial Analyst, Auditor (read-only) |
| `/accounts/`            | POST   | Create a new account         | Required       | Admin, Financial Analyst |
| `/accounts/{id}/`       | GET    | Retrieve account details     | Required       | Admin, Financial Analyst, Auditor (read-only) |
| `/accounts/{id}/`       | PUT    | Update account               | Required       | Admin, Financial Analyst |
| `/transactions/`        | GET    | List all transactions        | Required       | Admin, Financial Analyst, Auditor (read-only) |
| `/transactions/`        | POST   | Create a new transaction     | Required       | Admin, Financial Analyst |
| `/transactions/{id}/`   | GET    | Retrieve transaction details | Required       | Admin, Financial Analyst, Auditor (read-only) |
| `/transactions/{id}/`   | PUT    | Update transaction           | Required       | Admin, Financial Analyst |
| `/login/`               | POST   | Obtain auth token            | No             | Public |

---

## 📝 Sample Request (Create Account)

```http
POST /accounts/ HTTP/1.1
Host: transactionsapp-b3316d905d81.herokuapp.com
Authorization: Token <your_auth_token>
Content-Type: application/json

{
  "account_number": "1234567890",
  "account_name": "Savings Account",
  "user": 1,
  "account_type": "Savings",
  "balance": "1000.00"
}
```

---

## 🧪 Testing and Debugging

- Use **Postman** or `curl` to test API with token authentication  
- Check **Heroku logs** for errors:
  ```bash
  heroku logs --tail --app transactionsapp
  ```
- Run Django shell on Heroku for database inspection:
  ```bash
  heroku run python manage.py shell --app transactionsapp
  ```

---

