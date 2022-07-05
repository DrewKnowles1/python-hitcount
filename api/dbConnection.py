from cgi import print_arguments
from time import sleep
import mysql.connector
import os


#Putting the db connection thins into its own func
def mySQLConnect():

    host="0.0.0.0"
    user="root"
    password="secure"
    port="33060"

    if "MYSQLHOST" in os.environ :
        host = os.environ.get('MYSQLHOST')
    if "MYSQLUSER" in os.environ :
        user = os.environ.get('MYSQLUSER')
    if "MYSQLPWD" in os.environ :
        password = os.environ.get('MYSQLPWD')
    if "MYSQLPORT" in os.environ :
        port = os.environ.get('MYSQLPORT')
    
    
    mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        port = port,
    )
        

    return mydb



    
 
    
