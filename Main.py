from Classes import Drogues

# coding: utf-8

import sqlite3
import os
import re

# var d'env'
qualifier = re.sub(r'[-_]+', '', os.environ['BUILD_ID'])[0:12]

# connection
conn = sqlite3.connect('GenieKetamine')
cursor = conn.cursor()

# Insertion des données
data = {"nom": "ketamax", "prix": 30.19}
cursor.execute("""INSERT INTO DROGUE(nom, prix) VALUES(:nom, :prix)""", data)
ketamine = Drogues.Drogues("ketamine", 2.5)

print(ketamine)
print("Benjamin the boss!")
