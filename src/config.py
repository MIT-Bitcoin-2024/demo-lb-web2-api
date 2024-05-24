import os

import dotenv


dotenv.load_dotenv()


HOST = os.getenv('HOST', '127.0.0.1')
PORT = int(os.getenv('PORT', 8000))
