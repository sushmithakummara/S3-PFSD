#JSON files
#java script object notation
import json
"""data='{ "var1":"sushmitha","var2":"18"}'
#parsed=json.loads(data)
data={
    "channel_name":"codewithharry",
    "cars": ['bmw','audi a8','ferrari'],
    "fridge": ('roti',678,'dal')

}
#parsed=json.dumps(data)
print(parsed)"""
#sql lite3
#step-1:creating a connection to a sqlite database
import sqlite3
#given one made a connection object that used to interact with sqlite held in file aquarium.db,if that file not exit .sql automatically creates
connection=sqlite3.connect("aquarium.db")
#to check the file is succesfully created we use below one which gives output 0
print(connection.total_changes)
#step-2 adding data to sqlite database 1.table_name-fish...
cursor=connection.cursor()
cursor.execute("CREATE TABLE fish(name TEXT,species TEXT,tank_number INTEGER)")
cursor.execute("INSERT INTO fish VALUES('sammy','shark',1)")
cursor.execute("INSERT INTO fish  VALUES('jamie','cut',7)")
#reading data from sqlite
rows=cursor.execute("SELECT name,species,tank_number FROM fish").fetchall()
print(rows)