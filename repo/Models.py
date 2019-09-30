# Models.py BEGIN
#
#
#
###########################################################################
# + Importing Config.py BEGIN
###########################################################################
from Config import *
###########################################################################
# - Importing Config.py END
###########################################################################
#
#
#
###########################################################################
# + Controlling "__name__" Variable BEGIN
###########################################################################
control_name_variable(__name__)
###########################################################################
# - Controlling "__name__" Variable END
###########################################################################
#
#
#
###########################################################################
# + Time Class BEGIN
###########################################################################
class Time():
    def __init__(self,time):

        if isinstance(time, datetime):
            self.datetime = time
        else:
            self.datetime=datetime.fromtimestamp(time)

        self.year = self.datetime.year
        self.month = self.datetime.month
        self.day = self.datetime.day
        self.hour = self.datetime.hour
        self.minute = self.datetime.minute
        self.second = self.datetime.second
        self.microsecond = self.datetime.microsecond
        self.timestamp = self.datetime.timestamp()
    
    def __repr__(self):
        return "{:0>2d}.{:0>2d}.{} - {:0>2d}:{:0>2d}:{:0>d}.{}".format(self.day,self.month,self.year,self.hour,self.minute,self.second,self.microsecond)
###########################################################################
# - Time Class END
###########################################################################
#
#
#
###########################################################################
# + User Class BEGIN
###########################################################################
class User():
    def __init__(self,ID,username,password,firstname,lastname,created_date,creator,mail="",phone="",role=0):
        self.ID=ID
        self.username=username
        self.password=password
        self.firstname=firstname
        self.lastname=lastname
        self.mail=mail
        self.phone=phone
        self.active=True
        self.role=role
        self.created_date=created_date
        self.creator=creator   
###########################################################################
# - User Class END
###########################################################################
#
#
#
###########################################################################
# + Branch Class BEGIN
###########################################################################
class Branch():
    def __init__(self,ID,name,address="",phone=""):
        self.ID=ID
        self.name=name
        self.address=address
        self.phone=phone
###########################################################################
# - Branch Class END
###########################################################################
#
#
#
###########################################################################
# + Brand Class BEGIN
###########################################################################
class Brand():
    def __init__(self,ID,name):
        self.ID=ID
        self.name=name
###########################################################################
# - Brand Class END
###########################################################################
#
#
#
###########################################################################
# + Employee Class BEGIN
###########################################################################
class Employee():
    def __init__(self,ID,username,password,firstname,lastname,created_date,last_modified_date,creator,mail="",phone="",authority=0):
        self.ID=ID
        self.username=username
        self.password=password
        self.firstname=firstname
        self.lastname=lastname
        self.mail=mail
        self.phone=phone
        self.active=True
        self.authority=authority
        self.created_date=created_date
        self.creator=creator
        self.last_modified_date=last_modified_date
###########################################################################
# - Employee Class END
###########################################################################
#
#
#
###########################################################################
# + ProcessType Class BEGIN
###########################################################################
class ProcessType():
    def __init__(self,ID,name):
        self.ID=ID
        self.name=name
###########################################################################
# - ProcessType Class END
###########################################################################
#
#
#
###########################################################################
# + Process Class BEGIN
###########################################################################
class Process():
    def __init__(self,ID,amount,date,branch,brand,employee,processtype):
        self.ID=ID
        self.amount=amount
        self.date=date
        self.branch=branch
        self.brand=brand
        self.employee=employee
        self.processtype=processtype
###########################################################################
# - Process Class END
###########################################################################
#
#
#
###########################################################################
# + DatabaseHelper Class BEGIN
###########################################################################
class DatabaseHelper():
    def __init__(self,database_name):
        self.database_name=database_name
        self.connection=None

    def connect(self):
        self.connection=sqlite3.connect(self.database_name)
        return self.connection

    def get_cursor(self):
        return self.connection.cursor()

    def close(self):
        return self.connection.close()
###########################################################################
# - DatabaseHelper Class END
###########################################################################
#
# 
# 
# Models.py END