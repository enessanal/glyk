# Config.py BEGIN
#
#
#
###########################################################################
# + Controlling "__name__" Variable BEGIN
###########################################################################
if __name__ == "__main__":
    print("Exiting...\nRun this command => \"python main.py\"")
    exit()
###########################################################################
# - Controlling "__name__" Variable END
###########################################################################
#
#
#
###########################################################################
# + Controlling Python Version BEGIN
###########################################################################
try:
    import sys
except Exception as exception:
    print(str(exception))
    exit()

import sys

if sys.version_info.major is not 3:
    print("! Only Python3 !")
    exit()
###########################################################################
# - Controlling Python Version END
###########################################################################
#
#
#
###########################################################################
# + Controlling Libraries BEGIN
###########################################################################
moduleNames=[]

moduleNames.append("flask")
moduleNames.append("sqlite3")
moduleNames.append("argparse")
moduleNames.append("os")
moduleNames.append("os.path")
moduleNames.append("time")
moduleNames.append("datetime")
moduleNames.append("uuid")

try:
    import importlib
    for moduleName in moduleNames:
        if (importlib.util.find_spec(moduleName) is None):
            print('\nPlease install the "{}" module first.'.format(moduleName),end=" => ")
            print('pip3 install {}'.format(moduleName))
            exit()

except Exception as exception:
    from importlib import util
    for moduleName in moduleNames:
        if(util.find_spec(moduleName) is None):
            print('\nPlease install the "{}" module first.'.format(moduleName),end=" => ")
            print('pip3 install {}'.format(moduleName))
            exit()	

###########################################################################
# - Controlling Libraries END
###########################################################################
#
#
#
###########################################################################
# + Importing Standart Libraries BEGIN
###########################################################################
import os
import os.path
import time
from datetime import datetime
from uuid import uuid4
###########################################################################
# - Importing Standart Libraries END
###########################################################################
#
#
#
###########################################################################
# + Importing Third Party Libraries BEGIN
###########################################################################
import sqlite3
from flask import Flask
from flask import session
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import g
from flask import abort 
###########################################################################
# - Importing Third Party Libraries END
###########################################################################
#
#
#
###########################################################################
# + Helper Functions BEGIN
###########################################################################
def sprint(message):
    print("[+] "+str(message))

def iprint(message):
    print("[i] "+str(message))

def uprint(message):
    print("[-] "+str(message))


def redirectRoute(route):
  return redirect(url_for(route+"Route"))
###########################################################################
# - Helper Functions END
###########################################################################
#
#
#
###########################################################################
# + Configuration BEGIN
###########################################################################
DATABASE_PATH="glyk.db"
WEB_CLIENT_HOST="127.0.0.1"
WEB_CLIENT_PORT=8001
debugMode=False

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), './static')
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), './templates')
app = Flask(__name__)
app = Flask(__name__, static_folder=STATIC_DIR)
app.secret_key=os.urandom(10000)
###########################################################################
# - Configuration END
###########################################################################
#
#
#
# Config.py END