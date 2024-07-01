#!C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe
import MySQLdb
import cgi
from http import cookies as Cookie
import sys

print("Content-type: text/html\n")
print('''<html>
<head>
    <title>Login Status</title>
   <link rel="stylesheet" href="stylesheet.css">
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
    a = data.getvalue('e1')
    b = data.getvalue('p1')

    # Debug: print received form data
    print(f"<p>Received data - email: {a}, password: {b}</p>")

    # Prepare SQL query to fetch a record into the database.
    sql = "SELECT id, email, password FROM user WHERE email = %s AND password = %s"
    if cursor.execute(sql, (a, b)):
        # Commit your changes in the database
        db.commit()
        c = Cookie.SimpleCookie()

        # Assign a value
        c['mou'] = a

        # Set the expires time
        c['mou']['expires'] = 24 * 60 * 60

        # Print the header, starting with the cookie
        print(c)
        print("<h2>Successfully logged in</h2>")
    else:
        db.commit()
        print("<h2 class='error'>Failed to log in</h2>")
except Exception as e:
    # Rollback in case there is any error
    db.rollback()
    print(f"<h2 class='error'>Error occurred: {e}</h2>")
    print(f"<p>{sys.exc_info()}</p>")
finally:
    # Disconnect from server
    db.close()
    print('''
    </div>
</body>
</html>''')
