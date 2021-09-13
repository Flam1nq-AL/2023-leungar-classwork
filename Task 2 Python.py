import re
class Users:
    def __init__ (name_f,name_S,email,pword):
        self.First_Name = name_f
        self.Surname = name_S
        self.Email = email
        self.Password = pword
    
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'   
  
    if(re.search(regex,email)):   
        return True  
    else:   
        return False

def check_password(pword):
    regex = "^[a-z0-9A-Z]{6,12}$"

    if (re.search(regex,pword)):
        return True  
    else:
        return False


