import psycopg2


username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'

query_1 = '''
    CREATE VIEW books_by_year AS
        SELECT
            year_of_publication,
            COUNT(book_title) AS books_total
        FROM books
        GROUP BY year_of_publication;
'''
query_2 = '''
    CREATE VIEW books_after_2000 AS
        SELECT
            year_of_publication,
            COUNT(book_title) AS books_total,
            ROUND((COUNT(book_title) * 100.0) / SUM(COUNT(book_title)) OVER (), 1) AS percentage
        FROM books
        GROUP BY year_of_publication
        HAVING year_of_publication >= 2000;
'''
query_3 = '''
    CREATE VIEW ratings_by_ages AS
        SELECT
            age,
            book_rating
        FROM users
        JOIN ratings
        ON users.user_id = ratings.user_id;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    print('Кількість книг за роком публікації:')
    cur.execute('DROP VIEW IF EXISTS books_by_year')
    cur.execute(query_1)
    cur.execute('SELECT * FROM books_by_year')

    for row in cur:
        print(row)

    print('\nЧастка книг, виданих кожного року, починаючи з 2000, від усіх книг виданих з того ж часу:')
    cur.execute('DROP VIEW IF EXISTS books_after_2000')
    cur.execute(query_2)
    cur.execute('SELECT * FROM books_after_2000')

    for row in cur:
        print(row)

    print('\nРозподіл оцінок за віком користувачів:')
    cur.execute('DROP VIEW IF EXISTS ratings_by_ages')
    cur.execute(query_3)
    cur.execute('SELECT * FROM ratings_by_ages')

    for row in cur:
        print(row)
