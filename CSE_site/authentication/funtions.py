import re

def validateEmailStudent(email):
    regex = r'^[a-z\d\.]+@bmsce.ac.in$'
    return re.match(regex, email)

def validateEmailFaculty(email):
    regex = r'^[a-z\.]+@bmsce.ac.in$'
    return re.match(regex, email)

def validatePassword(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'
    return re.match(regex, password)