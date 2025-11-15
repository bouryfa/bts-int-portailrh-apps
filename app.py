from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_db_connection, init_db
from config import Config
import sys

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

@app.route('/')
def index():
    """Display list of all employees"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees ORDER BY created_at DESC")
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', employees=employees)
    except Exception as e:
        flash(f'Error loading employees: {str(e)}', 'danger')
        return render_template('index.html', employees=[])

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    """Add a new employee"""
    if request.method == 'POST':
        try:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            position = request.form.get('position')
            department = request.form.get('department')
            phone = request.form.get('phone')
            hire_date = request.form.get('hire_date')

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO employees
                (first_name, last_name, email, position, department, phone, hire_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, email, position, department, phone, hire_date))
            conn.commit()
            cursor.close()
            conn.close()

            flash('Employee added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error adding employee: {str(e)}', 'danger')
            return redirect(url_for('add_employee'))

    return render_template('add_employee.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    """Edit an existing employee"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        try:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            position = request.form.get('position')
            department = request.form.get('department')
            phone = request.form.get('phone')
            hire_date = request.form.get('hire_date')

            cursor.execute("""
                UPDATE employees
                SET first_name=%s, last_name=%s, email=%s, position=%s,
                    department=%s, phone=%s, hire_date=%s
                WHERE id=%s
            """, (first_name, last_name, email, position, department, phone, hire_date, id))
            conn.commit()
            cursor.close()
            conn.close()

            flash('Employee updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error updating employee: {str(e)}', 'danger')

    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cursor.fetchone()
    cursor.close()
    conn.close()

    if not employee:
        flash('Employee not found!', 'danger')
        return redirect(url_for('index'))

    return render_template('edit_employee.html', employee=employee)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_employee(id):
    """Delete an employee"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Employee deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting employee: {str(e)}', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'init':
        init_db()
    else:
        app.run(debug=Config.DEBUG, host='0.0.0.0', port=5000)
