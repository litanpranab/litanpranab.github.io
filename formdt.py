import cgi
form = cgi.FieldStorage()
first_name = form.getvalue('first_name')
print(first_name)