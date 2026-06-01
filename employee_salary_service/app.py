from flask import Flask, render_template, request
from db import conn, cursor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():

    name = request.form['name']
    base_salary = float(request.form['base_salary'])
    hours_worked = float(request.form['hours_worked'])

    # Bonus = 10% of base salary
    bonus = base_salary * 0.10

    # Overtime Pay
    overtime_pay = 0

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * 500

    total_salary = base_salary + bonus + overtime_pay

    query = """
    INSERT INTO employees
    (name, base_salary, hours_worked, bonus, overtime_pay, total_salary)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        name,
        base_salary,
        hours_worked,
        bonus,
        overtime_pay,
        total_salary
    )

    cursor.execute(query, values)
    conn.commit()

    return render_template(
        'index.html',
        name=name,
        base_salary=base_salary,
        hours_worked=hours_worked,
        bonus=bonus,
        overtime_pay=overtime_pay,
        total_salary=total_salary
    )

if __name__ == '__main__':
    app.run(debug=True)