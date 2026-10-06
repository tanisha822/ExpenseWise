# ExpenseWise – Personal Expense & Analytics System

ExpenseWise is a Django-based personal expense management and analytics web application. It helps users record, manage, search, filter and analyze their daily expenses through a simple and user-friendly dashboard.

## Features

* User Signup and Login
* Secure User Authentication
* Add New Expenses
* Edit Expenses
* Delete Expenses
* Search Expenses
* Category-wise Filtering
* Date-wise Filtering
* Total Expense Calculation
* Average Expense Calculation
* Monthly Expense Analysis
* Category-wise Expense Analysis
* Monthly Budget Management
* Remaining Budget Tracking
* Budget Status Monitoring
* Interactive Expense Analytics

## Technologies Used

* Python
* Django
* SQLite
* HTML
* CSS
* JavaScript
* Chart.js
* Git
* GitHub

## Project Structure

```text
ExpenseWise/
│
├── accounts/
├── expenses/
├── expensewise/
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```text
git clone https://github.com/tanisha822/ExpenseWise.git
```

### 2. Open the project folder

```text
cd ExpenseWise
```

### 3. Create and activate virtual environment

```text
python -m venv .venv
```

Windows:

```text
.venv\Scripts\activate
```

### 4. Install dependencies

```text
pip install -r requirements.txt
```

### 5. Run migrations

```text
python manage.py migrate
```

### 6. Start the development server

```text
python manage.py runserver
```

Then open the local development server in your browser.

## Main Modules

### Authentication

Users can create an account, log in and log out securely.

### Expense Management

Users can add, edit and delete their personal expenses.

### Search and Filters

Expenses can be searched by title and filtered using category and date range.

### Budget Management

Users can set a monthly budget and track their spending against it.

### Analytics

The dashboard provides total expenses, average expense, monthly analysis and category-wise analysis.

## Future Improvements

* MySQL database integration
* Expense export to CSV/PDF
* Advanced analytics
* Email notifications
* Deployment
* Mobile-friendly improvements

## Author

Tanisha Barik

B.Tech – Computer Science & Engineering

Python | Django | SQL | Data Analytics
