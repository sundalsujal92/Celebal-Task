

## 📌 Project Overview

This project demonstrates a **3-Tier Web Application Architecture** with the following components:

| Tier | Component        | Technology                     |
| ---- | ---------------- | ------------------------------ |
| Web  | Frontend Website | IIS (Windows) + Apache (Linux) |
| App  | API Backend      | Python Flask                   |
| DB   | Logging Database | SQL Server                     |

---

## 🧱 Architecture Layout

* Each tier is hosted in **a separate Virtual Network and Subnet**:

  * `VNet-Web` → `Subnet-Web` → IIS/Apache (index.html)
  * `VNet-App` → `Subnet-App` → Flask API (`/log`)
  * `VNet-DB`  → `Subnet-DB`  → SQL Server (logs table)

---

## 🔒 Network Security Requirements

* ❌ **No outbound internet access** after provisioning packages and installations.
* ✅ **Inbound internet allowed only** for:

  * Web Tier (HTTP access)
  * App Tier (API access from Web tier)
* 🔒 **No private connectivity** between tiers **unless essential**.
* 📛 **Each subnet must have an individual NSG** (Network Security Group).

---

## 💡 How It Works

1. **User clicks a button** on the `index.html` page.
2. JavaScript sends a **POST** request to the Flask API (`/log`).
3. The API logs a **timestamp + message** to the SQL Server database.

---

## 🚀 Deployment Steps

### 🔹 1. Web Tier (IIS / Apache)

* Host `web/index.html` on both:

  * IIS Server (Windows VM)
  * Apache Server (Linux VM)
* Replace `APP_TIER_IP` in the HTML with the **App tier's IP**.

---

### 🔹 2. App Tier (Flask API)

* Install Python and required packages:

  ```bash
  pip install -r app/requirements.txt
  ```
* Edit `app/app.py` and replace:

  * `DB_TIER_IP`
  * `your_username`
  * `your_password`
* Run the API:

  ```bash
  python3 app.py
  ```

---

### 🔹 3. DB Tier (SQL Server)

* Execute `db/init.sql` to:

  * Create `web_logs` database
  * Create `logs` table:

    ```sql
    CREATE TABLE logs (
        id INT PRIMARY KEY IDENTITY(1,1),
        timestamp DATETIME,
        message NVARCHAR(255)
    );
    ```

---

## ✅ Validation

* Visit your Web Tier's IP in a browser.
* Click the **Log Action** button.
* Verify the entry in the SQL table using:

  ```sql
  SELECT * FROM logs;
  ```

---

## 📁 Folder Structure

```
Celebal-Task-3-Tier/
├── web/
│   └── index.html
├── app/
│   ├── app.py
│   └── requirements.txt
├── db/
│   └── init.sql
└── README.txt
```

---


