from Classes import Drogues

# coding: utf-8

import sqlite3
import os

# var d'env'
qualifier = os.environ['QUALIFIER']
# connection
conn = sqlite3.connect('GenieKetamine')
cursor = conn.cursor()

# Insertion des données
data = {"nom": "ketamax", "prix": 30.19}
cursor.execute("""INSERT INTO DROGUE(nom, prix) VALUES(:nom, :prix)""", data)
ketamine = Drogues.Drogues("ketamine", 2.5)

print(ketamine)
