from Classes import Drogues

# coding: utf-8

import sqlite3

# connection
conn = sqlite3.connect('genieketamine.db')
cursor = conn.cursor()

# Insertion des données
data = {"name": "olivier", "age": 30}
cursor.execute("""INSERT INTO users(name, age) VALUES(:name, :age)""", data)
ketamine = Drogues.Drogues("ketamine", 2.5)

print(ketamine)
