import psycopg2
import csv


username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'
CSV_BOOKS_FILE = 'Books.csv'
CSV_USERS_FILE = 'Users.csv'
CSV_RATINGS_FILE = 'Ratings.csv'
files = [CSV_BOOKS_FILE, CSV_USERS_FILE, CSV_RATINGS_FILE]


query_1 = '''
    INSERT INTO books (ISBN, book_title, book_author, year_of_publication, publisher, 
        image_URL_s, image_URL_m, image_URL_l) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
'''
query_2 = '''
    INSERT INTO users (user_ID, age, location_1, location_2, location_3) VALUES (%s, %s, %s, %s, %s);
'''
query_3 = '''
    INSERT INTO ratings (user_ID, ISBN, book_rating) VALUES (%s, %s, %s);
'''

query_4 = '''
    DELETE FROM books;
'''
query_5 = '''
    DELETE FROM users;
'''
query_6 = '''
    DELETE FROM ratings;
'''

queries = (query_1, query_2, query_3)

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute(query_4)
    cur.execute(query_5)
    cur.execute(query_6)

    for file, query in zip(files, queries):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            # Add the first 20 rows to each table
            for idx, row in enumerate(reader):
                if idx < 20:
                    values = tuple(row.values())
                    cur.execute(query, values)
                else:
                    break

    conn.commit()
