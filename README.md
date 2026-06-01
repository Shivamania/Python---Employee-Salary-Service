# Employee Salary Service

Python Flask Project developed during TCS Initial Learning Program (ILP): A web-based Employee Salary Service application that calculates employee salaries and stores records in a MySQL database.

## Introduction

Employee Salary Service is a web application that allows users to calculate employee salaries based on base salary, bonus, and overtime hours. The application provides a user-friendly interface for entering employee details, calculating salary components, and storing records in a MySQL database.

## Features

- Calculate employee salary based on base salary
- Calculate bonus salary automatically
- Calculate overtime pay based on hours worked
- Display total salary instantly
- Store employee salary records in MySQL database
- User-friendly web interface with form validation

## Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript

## Usage

1. Run the Flask application.
2. Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

3. Enter employee details:
   - Employee Name
   - Base Salary
   - Hours Worked
4. Click the **Calculate Salary** button.
5. View the calculated salary details including:
   - Bonus Salary
   - Overtime Pay
   - Total Salary

## Project Structure

```text
employee_salary_service/
│
├── app.py
├── db.py
├── templates/
│   └── index.html
└── README.md
```

## Flask Concepts Used

### Flask Components

- **Flask**: Creates the web application instance.
- **render_template()**: Renders HTML pages dynamically.
- **request**: Retrieves form data submitted by users.

### Routing

- **@app.route('/')**: Maps requests to the home page.
- **@app.route('/calculate', methods=['POST'])**: Handles salary calculation requests submitted through the form.

### Database Integration

- MySQL database connectivity using `mysql-connector-python`
- SQL INSERT operations for storing employee records
- Database transaction management using `commit()`

## Future Enhancements

- Employee login and authentication
- Salary history tracking
- Payslip generation
- Employee search functionality
- REST API integration

## Contact

**Name:** Shivam Patel

**GitHub:** Shivamania
