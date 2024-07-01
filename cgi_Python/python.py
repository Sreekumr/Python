#!C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe
import cgi
print("Content-type: text/html\n\n")
# This line sends an HTTP header specifying that the content is HTML.

# Import the Common Gateway Interface (CGI) module to handle form data.

form = cgi.FieldStorage()
# Create a FieldStorage object to parse and store the data submitted via the form.

username = form.getvalue("username")
# Retrieve the value associated with the "username" field from the form data.

# HTML header
print('''<html>
<head>
    <link rel="stylesheet" href="welcome.css">
    <title>Success Page</title>
</head>
<body>
    <h2>Successfully logged in</h2>
</body>
</html>''')


# Format the username with <strong> and <span> for larger text
print("<p><strong><span style='font-size: 20px;'>{}</span></strong> Congratulations !!,<br></p>".format(username))
# Display a congratulatory message with the submitted username in larger text.

# Print the second line on a new line
print("<p>You have successfully sent data from an HTML form to a CGI Python script.</p>")
# Display a message indicating that the form data was successfully processed.

# Close the HTML tags
print("</body>")
print("</html>")
