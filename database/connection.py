from distutils.command.config import config
from mysql import connector
config={
    'user':'root',
    'password': '12345678',
    'host': 'localhost',
    'database':'ejemplo2'
}

def create_conection():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Error at create_connection function: {err.msg}")
    return conn