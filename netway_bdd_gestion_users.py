##### CREATION D'UTILISATEURS #####

# Importation des modules python
import random
import string
import mariadb

# Importation des fichiers python
from netway_menu import *
# import netway_menu from 


#MDP aleatoire
# liste_characteres=string.ascii_letters+string.digits
# pwd=""

# for i in range(12):
#      pwd+=liste_characteres[random.randint(0, len(liste_characteres)-1)]



# Création d'un utilisateur en BDD
def creation_usr_bdd(cur, conn, role, site):
    queryOk = False
    # UTILISER LE LOGIN POUR LA SUITE
    checklogin = checkLogin(cur, role, site) #checkmail contient une valeur booléenne et l'id de l'utilisateur 

    if checklogin[0] == True:
        print("Un utilisateur possède déjà ce login, veuillez saisir un login différent.")
        creation_usr_bdd(cur,conn, role, site) # Rappel de la fonction en cours en cas de login déjà présent en bdd
    else:
        # Définition des variables
        user_name = input("Prénom d'utilisateur : ").lower()
        user_lastname = input("Nom de famille de l'utilisateur : ").lower()
        user_email = checklogin[2] + "@teamnetway.com"
        user_role = input("Type d'utilisateur (2- admin, 3- Utilisateur) : ")
        if(role == 1):
            site = input("Site de l'utilisateur (paris, rennes, strasbourg, grenoble) : ")
        # user_pwd = pwd
        mdprandom = "mdprandom"
        query = f"INSERT INTO utilisateurs (prenom,nom,email,role,login,password, site) VALUES ('{user_name}', '{user_lastname}', '{user_email}', '{user_role}', '{checklogin[2]}', '{mdprandom}', '{site}')"
        
        try: 
            cur.execute(query)      # Préparation de la requête SQL
            conn.commit()           # Envoi de la requête a la base de donnée
            queryOk = True
        except mariadb.Error as e: 
            print(f"Error: {e}")

        if(queryOk):
            print(f"L'utilisateur {user_name} {user_lastname} a bien été créé !")
            print(f"L'adresse mail associée à ce compte est : {user_email}")

        else : 
            print("Erreur lors de la création de l'utilisateur, veuillez contacter votre administrateur réseau.")

# Modification d'un utilisateur en BDD
def modif_usr_bdd(cur, conn, role, site, id):
    # Définition des variables
    queryOk = False
    user_name = input("Prénom d'utilisateur : ").lower()
    user_lastname = input("Nom de famille de l'utilisateur : ").lower()
    # user_login = user_name[0] + user_lastname
    # user_email = login + "@teamnetway.com"
    # user_pwd = pwd
    user_role = input("Type d'utilisateur (2- admin, 3- Utilisateur) : ")
    if(role == 1):
            site = input("Site de l'utilisateur (paris, rennes, strasbourg, grenoble) : ")
    mdprandom = "mdprandom"
    query = f"UPDATE utilisateurs SET prenom='{user_name}', nom='{user_lastname}', password='{mdprandom}', role='{user_role}', site='{site}' WHERE id={id}"
    
    try: 
        cur.execute(query)      # Préparation de la requête SQL
        conn.commit()           # Envoi de la requête a la base de donnée
        queryOk = True
    except mariadb.Error as e: 
        print(f"Error: {e}")

    if(queryOk):
        print(f"L'utilisateur {user_name} {user_lastname} a bien été modifié !")
    else : 
        print("Erreur lors de la modification de l'utilisateur, veuillez contacter votre administrateur système.")

# Suppression d'un utilisateur en BDD
def suppr_usr_bdd(cur, conn, id):
    queryOk = False
    query = f"DELETE FROM utilisateurs WHERE id = {id}"

    try:
        cur.execute(query)      # Préparation de la requête SQL
        conn.commit()           # Envoi de la requête a la base de donnée
        queryOk = True
    except mariadb.Error as e: 
        print(f"Error: {e}")

    if(queryOk):
        print(f"L'utilisateur a bien été supprimé !")
    else : 
        print("Erreur lors de la modification de l'utilisateur, veuillez contacter votre administrateur système.")

# Vérification de l'existance du login en bdd
def checkLogin(cur, role, site):
    login = input("Veuillez saisir le login : ").lower()
    query = f"SELECT id, count(*) AS nb FROM utilisateurs WHERE login='{login}' "
    if(role != 1):
        query = query + f"AND site='{site}'"
    cur.execute(query)
    for(id, nb) in cur: 
        if(nb > 0):
            return (True,id, login)
        else:
            return (False, id, login)
            
def getListUser(cur, conn, role, site):

    query = f"SELECT login, prenom, nom, email, role, site from utilisateurs "
    if(role != 1):
        query = query + f"WHERE site='{site}' "
    query = query + "ORDER BY role ASC"
    print(query)
    cur.execute(query)
    print(" ____________________________________________________________________________________________________________________________________________________________ ")
    print(f"|   {'login':20}   |   {'prenom':20}   |   {'nom':20}   |   {'email':40}   |   {'role':5}   |   {'site':10}   |")
    print("|------------------------------------------------------------------------------------------------------------------------------------------------------------|")
    for(login, prenom, nom, email, role, site) in cur:
        print(f"|   {login:20}   |   {prenom:20}   |   {nom:20}   |   {email:40}   |   {role:5}   |   {site:10}   |")
    print("|____________________________________________________________________________________________________________________________________________________________|")
    