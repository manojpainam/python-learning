'''
Encapsulation -
            Encapsulation is the protecting the data inside a class
            It means keep the data and methods together inside a class.

            private porpeties can be created by using __ prefix 
'''

class User:
    def __init__(self, name, password):
       self.name = name
       self.__password = password

    #private properties can only be accessed by get method
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        if len(password) < 6:
            return "Password must be minimum 6 digit length"
        else:
            self.__password = password
            return "password set successfully!!!"
    
    # under_score before the method names are intendted to tell the other developers that this method is for intername purpose
    def _user_details(self):
        return "User : {}, password: {}".format(self.name, self.__password)

user = User("Manoj", "{x54G2f%Ul3yQv&q=^6b2-lS^5yEC-")
#this will raise an error as it is a private properti
#print(user.__password)

#getting the password using get method
print(user.name, user.get_password())
print(user.set_password("5(g;k_;Y!GRpFh1dgASb6[fX3vcC}g"))
print(user.name, user.get_password())

print(user._user_details())

