#!C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe
import MySQLdb
import cgi
import sys

print("Content-type: text/html\n")
print('''<html>
<head>
    <title>Registration Status</title>
    <link rel="stylesheet" href="stylesheet.css"> <!-- Assuming you have a stylesheet for styling -->
</head>
<body>
<div class="container">''')

try:
    # Open database connection
    db = MySQLdb.connect("localhost", "root", "", "student")
    print("<p>Database connection successful.</p>")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()
    data = cgi.FieldStorage()
    name = data.getvalue('name')
    email = data.getvalue('email')
    college = data.getvalue('college')
    age = data.getvalue('age')
    password = data.getvalue('password')
    confirm_password = data.getvalue('confirm_password')

    # Debug: print received form data
    print(f"<p>Received data - Name: {name}, Email: {email}, College: {college}, Age: {age}</p>")

    # Check if passwords match
    if password != confirm_password:
        raise Exception("Passwords do not match")

    # Insert data into MySQL
    sql = "INSERT INTO user (name, email, college, age, password) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (name, email, college, age, password))
    db.commit()

    print("<h2>Registration successful</h2>")
except Exception as e:
    # Rollback in case there is any error
    db.rollback()
    print(f"<h2 class='error'>Error occurred during registration: {e}</h2>")
    print(f"<p>{sys.exc_info()}</p>")
finally:
    # Disconnect from server
    db.close()
    print('''
    </div>
</body>
</html>''')
