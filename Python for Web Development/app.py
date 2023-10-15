import sqlite3

connect = sqlite3.connect('data.db')
                          
connect.execute('''CREATE TABLE COSTUMER
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL);''')
               
connect.close() 