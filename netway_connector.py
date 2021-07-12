# Le f = Permet d'afficher les variables dans un print

# Importation des modules
import mariadb
import sys

# Connexion à la BDD
try:
    conn = mariadb.connect(
        user="connector",
        password="ESGI@2021",
        host="localhost",
        port=3306,
        database="bdd_python"
    )

# Message d'erreur la connexion à la BDD n'a été établie
except mariadb.Error as e:
    print(f"Impossible de se connecter avec la BDD ! : {e}")
    sys.exit(1)

# Message si la connexion à la BDD a été établie
cur = conn.cursor()

print(f"Connexion établie avec la base de données !")