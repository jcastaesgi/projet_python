# Importation des modules
import mariadb, sys

# Import fichiers python
# from netway_menu import menu, menu_admin, menu_user
from netway_menu import *
# from netway_ftp import *

# Connexion à la BDD
try:
    conn = mariadb.connect(
        user="connector",
        password="ESGI@2021",
        host="localhost",
        port=3306,
        database="bdd_python"
    )

# Retour msg d"erreur si connexion NOT OK
except mariadb.Error as e:
    print(f"Impossible de se connecter avec la BDD : {e}")
    sys.exit(1)

# Cur correspond au curseur des requêtes
cur = conn.cursor()


def authentification():
    # DEFINITION DES VARIABLES
    login = input("Nom d'utilisateur : ") #Stokage dans une variable le login
    mdp = input("Mot de passe : ") #Stokage dans une variable le password
    user_role = ""
    is_connected = False

    cur.execute("SELECT count(*) AS nb, role, site FROM utilisateurs WHERE login=? AND password=?",(login, mdp))
    for(nb,role, site) in cur:
        user_role = role
        site_user = site
        if(nb > 0):
            is_connected = True


    # Affichage connexion OK
    if(is_connected == True):
        print("Vous êtes bien identifié")
        return (user_role, site_user)
    else:
        print("Impossible de vous connecter, merci de réessayer.")
        authentification()

print("Bienvenue sur notre application, Merci de bien vouloir vous authentifier.")

infoAuth = authentification()
# print(role)

menu(cur, conn, infoAuth[0], infoAuth[1])