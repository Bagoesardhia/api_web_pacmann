import psycopg2

conn = psycopg2.connect(
        host="209.97.172.45",
        port='5510',
        database="dev",
        user="dev",
        password= "dev123"
        )

def connection():
    try:
        conn
        return 0
    except Exception as e:
        return 1
