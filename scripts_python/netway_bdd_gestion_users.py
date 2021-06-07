##### CREATION D'UTILISATEURS #####

# Importation des modules python
import random
import string

# Importation des fichiers python
from netway_login_bdd import cur

#MDP aleatoire
liste_characteres=string.ascii_letters+string.digits
pwd=""

for i in range(12):
     pwd+=liste_characteres[random.randint(0, len(liste_characteres)-1)]


# Définition des variables
user_name = input("Prénom d'utilisateur : ").lower()
user_lastname = input("Nom de famille de l'utilisateur : ").lower()
user_pwd = pwd
user_email = user_name + "." + user_lastname + "@teamnetway.com"
user_role = input("Type d'utilisateur (2- admin, 3- Utilisateur) : ")
user_login = user_name[0] + user_lastname

# Création d'un utilisateur en BDD
cur.execute("SELECT count(*) AS nb, role FROM utilisateurs WHERE ",(user_name,user_lastname,user_pwd,user_email,user_role,user_login))

# Affichage création de l'utilisateur
print("L'utilisateur suivant vient d'être crée :")
print("Prénom :",user_name)
print("Nom :",user_lastname)
print("Pwd :",pwd)
print("@ :",user_email)
print("Rôle :",role_user)
print("Login utilisateur :",user_login)
