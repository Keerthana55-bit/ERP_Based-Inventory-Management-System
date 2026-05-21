import sqlite3
import pytest
from employee import employeeClass
from tkinter import Tk

@pytest.fixture
def app():
    root = Tk()
    app = employeeClass(root)
    return app

def test_add_employee(app):
    # Setup test data
    app.var_emp_id.set("E001")
    app.var_name.set("Test User")
    app.var_email.set("test@example.com")
    app.var_gender.set("Male")
    app.var_contact.set("1234567890")
    app.var_dob.set("01-01-2000")
    app.var_doj.set("01-01-2024")
    app.var_pass.set("password")
    app.var_utype.set("Admin")
    app.txt_address.insert("1.0", "Test Address")
    app.var_salary.set("50000")

    # Call add method
    app.add()

    # Verify in database
    con = sqlite3.connect("ims.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM employee WHERE eid=?", ("E001",))
    row = cur.fetchone()
    assert row is not None
    assert row[1] == "Test User"
