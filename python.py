# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
import hashlib
from getpass import getpass
import re
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def check(email):
 
    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, email)):
        print("Valid Email")
        return email
 
    else:
        print("Invalid Email")

# ########## Authentification utilisateur #########
print("Bienvenue sur notre application, Merci de bien vouloir vous authentifier.")
login = input("Nom d'utilisateur : ") #Stokage dans une variable le login
mdp = getpass("Mot de passe : ") #Stokage dans une variable le password
print("Merci, nous vérifions votre compte")
print(mdp)

#concat login 
prenom = input("saisir votre prenom")
nom = input("saisir votre nom")
login = prenom[0] + nom


#verif email
email = input("email : ")
if(check(email)):
    emailValid = email
# else: 
#     email = input("email non valide, merci de saisir un email valide ")

print(prenom, nom, login, emailValid)



######### Fin authentification utilisateur #########

# Python program to validate an Email
 
# import re module
 
# re module provides support
# for regular expressions
 
# Make a regular expression
# for validating an Email
 
# Define a function for
# for validating an Email
 
 

 
 
# Driver Code
if __name__ == '__main__':
 
    # Enter the email
    email = input("email : ")
    check(email)
 
