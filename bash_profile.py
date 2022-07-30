import os
import sys
# import dotenv

# from pathlib import Path
# from dotenv import load_dotenv

# env_path = Path('~/.zshrc')
# load_dotenv(dotenv_path=env_path)

email = os.environ.get("GMAILADDRESS")
password = os.environ.get("GMAILPW")

print(email, password)
# print(sys.path)
# print(os.environ['PYTHONPATH'])
# print(os.environ['GMAILADDRESS'])
# print(os.environ['GMAILPW'])
# print(os.environ)
