import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='test',
    user='postgres',
    password='Ane4ka18230'
)
try:
    with conn:
        with conn.cursor() as cur:
            # execute query
            cur.execute('insert into user_account values (%s, %s)', (6, 'Jake'))

            cur.execute('select * from user_account')
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()
