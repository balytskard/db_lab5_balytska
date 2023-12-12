import csv
import psycopg2


username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'

output_file = 'new_{}.csv'
tables = ['users', 'books', 'ratings']


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with conn:
    cur = conn.cursor()

    for table in tables:
        cur.execute('SELECT * FROM ' + table)
        field_names = [x[0] for x in cur.description]

        with open(output_file.format(table), 'w', newline='') as new_csv:
            writer = csv.writer(new_csv)
            writer.writerow(field_names)

            for row in cur:
                writer.writerow(row)
