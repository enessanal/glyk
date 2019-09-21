class Employee():
    def __init__(self,ID,username,password,firstname,lastname,mail="",phone="",authority=0):
        self.ID=ID
        self.username=username
        self.password=password
        self.firstname=firstname
        self.lastname=lastname
        self.mail=mail
        self.phone=phone
        self.active=True
        self.authority=authority        