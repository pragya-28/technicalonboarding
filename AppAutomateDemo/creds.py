import os
import sys
from dotenv import load_dotenv

try:
	bash_script_path = 'run.sh'
	load_dotenv(bash_script_path)
except:
	pass

BROWSERSTACK_EMAIL = os.environ.get('BROWSERSTACK_EMAIL')
BROWSERSTACK_PWD = os.environ.get('BROWSERSTACK_PWD')

BROWSERSTACK_USERNAME = os.environ.get('BROWSERSTACK_USERNAME')
BROWSERSTACK_ACCESS_KEY = os.environ.get('BROWSERSTACK_ACCESS_KEY')