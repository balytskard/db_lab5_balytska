import json
import psycopg2


username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'

tables = ['users', 'books', 'ratings']


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


data = {}
with conn:

    cur = conn.cursor()
    
    for table in tables:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        field_names = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(field_names, row)))

        data[table] = rows


with open('data.json', 'w') as outf:
    json.dump(data, outf, default = str)
