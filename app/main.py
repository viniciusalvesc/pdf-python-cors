import os
from config.initialize import create_app
from dotenv import load_dotenv

load_dotenv()

def main():
    app = create_app()
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))

if __name__ == '__main__':
    main()