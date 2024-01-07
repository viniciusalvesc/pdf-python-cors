import os
from config.database import create_db_connection
from config.initialize import create_app
from dotenv import load_dotenv
from decouple import config
# from app.config.conf import HOST, PORT

load_dotenv()

def main():
    try:
        app = create_app()

        db_connection = create_db_connection()

        if db_connection:
            print('conectou ao banco do tax')
            app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
            db_connection.close()
        else: print('não conectou')
    
    except Exception as e:
        print(f'[__main__]: {e}')

if __name__ == '__main__':
    main()