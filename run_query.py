import psycopg2
import cred
import conn

# Set Redshift cluster connection details
dbname = conn.database
host = conn.host
port = conn.port

user = cred.db_user
password = cred.password

# Connect to AWS Redshift database
connect = psycopg2.connect(database=dbname,
                           host=host,
                           port=port,
                           user=user,
                           password=password)

cur = connect.cursor()

# SQL Query

cur.execute("CREATE TABLE public.test4 "
            "(col1 varchar,"
            "col2 varchar,"
            "col3  varchar);")

connect.commit()

cur.close()
connect.close()
