# https://www.dotenv.org/docs/security/env

from dotenv import load_dotenv
import os

load_dotenv()
app_password = (os.environ.get('app_password'))
