import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage() # stores data into fields

usrName = form.getvalue('username')  # getting the data from the fields
pWord = form.getvalue('password')

# creates html
print("""Content-type:text/html\r\n\r\n
    <html>
    <head><title>Login</title></head>
    <body>
    <h1>Login Success!</h1>
    <b>Username: </b> %s <br>
    <br><b>Password: </b> %s <br>
    </div>
    </body>
    </html>""" % (usrName, pWord))