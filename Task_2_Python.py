
import re


class Users:
    def __init__(self, first_name, surname, email, password):
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.password = password

    def check_email(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if(re.search(regex, email)):
            print('Valid Email')
        else:
            print('Invalid Email')

    def check_password(self, password):
        regex2 = '^[a-zA-Z0-9]*$'
        regex3 = '^\w{6,12}$'

        if (re.search(regex2, password)) and (re.search(regex3, password)):
            print('Valid Password')
        else:
            print('Invalid Password')


adrian = Users('Adrian', 'Leung', 'adrianleung@live.com', 'Hihi12345')
adrian.check_password(adrian.password)
adrian.check_email(adrian.email)
>>>>>> > 147d255dcb781f6eea98f6888113d05b91d30d1c
