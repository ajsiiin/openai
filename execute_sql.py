import pyodbc

def execute_sql(sql_query):
    conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=server;DATABASE=db;UID=user;PWD=password;")
    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    result = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    cursor.close()
    conn.close()
    return result