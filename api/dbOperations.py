from dbConnection import mySQLConnect

def initialiseDB():

    mydb = mySQLConnect()
    mycursor = mydb.cursor() 

    mycursor.execute("CREATE DATABASE IF NOT EXISTS HITCOUNT")
    mycursor.execute("USE HITCOUNT")
    mycursor.execute("CREATE TABLE IF NOT EXISTS CountAPIHits (counter VARCHAR(255), hits int)")
    #Initialise a new counter Record if it doesnt already exist, so we can initialise on first run, without destroying any old data should it exist
    mycursor.execute("INSERT INTO CountAPIHits(counter, hits) SELECT * FROM (SELECT 'counter1' as counter, 0 as hits) AS new_value WHERE NOT EXISTS (SELECT counter FROM CountAPIHits WHERE counter = 'counter1') LIMIT 1")

    mydb.commit()
    mycursor.close()
    mydb.close()

    


def incrimentDBRecord():
    
    mydb = mySQLConnect()
    mycursor = mydb.cursor()

    mycursor.execute("USE HITCOUNT")
    mycursor.execute("UPDATE CountAPIHits SET hits = hits + 1 WHERE counter = 'counter1'")
    mycursor.execute("SELECT hits FROM CountAPIHits where counter = 'counter1'")
    #Get one element
    record =  mycursor.fetchone()
    response = record[0]

    mydb.commit()
    mycursor.close()
    mydb.close()

    return response