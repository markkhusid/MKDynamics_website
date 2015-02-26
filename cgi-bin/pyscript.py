#!/usr/bin/python3.4

#import cgi
import cgitb
cgitb.enable()

import os

#print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: text/html")
print()

print("Hello World!")

#os.system('./fortran_practice > fortran_output.html')


print()

#print(" <html> <body> this is a test </body> </html> ")


print ("""
<html>
<body>
<h2>Hello World!</h2>
<h2>This script will eventually activate a Fortran program that performs the energy calculations</h2>
<h2>I am still trying to sort out linux permissions and firewall settings to allow a server side script to run</h2>


</body>
</html>
""")


