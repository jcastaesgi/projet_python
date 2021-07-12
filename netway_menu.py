# Import des modules
# from netway_scan_port import check_ports_connus
from netway_bdd_gestion_users import creation_usr_bdd, checkLogin, modif_usr_bdd, suppr_usr_bdd, getListUser
from netway_scan_port import scanports_auto, scanports_manuel
# from netway_ftp import *

## MENU GESTION BDD ##
def menu_gestion_users_bdd(cur,conn,role, site):
    print("\n################################")
    print("# [1] Créer un utilisateur     #")
    print("# [2] Modifier un utilisateur  #")
    print("# [3] Supprimer un utilisateur #")
    print("# [4] Liste des utilisateurs   #")
    print("# [0] Retour au menu principal #")
    print("################################\n")

    # menu_gestion_users_bdd()
    option = int(input("Choisissez une option : "))

    if option == 1:
        creation_usr_bdd(cur, conn,role, site)
    elif option == 2:
        checklogin = checkLogin(cur, role, site) #checklogin contient une valeur booléenne et l'id de l'utilisateur 
        if checklogin[0] == True:
            modif_usr_bdd(cur, conn, role, site, checklogin[1]) 
        else:
            print("Aucun utilisateur trouvé avec ce login, veuillez saisir un login connu.")
            menu_gestion_users_bdd(cur,conn, role, site)
    elif option == 3:
        checklogin = checkLogin(cur, role, site) #checklogin contient une valeur booléenne et l'id de l'utilisateur 
        if checklogin[0] == True:
            suppr_usr_bdd(cur, conn, checklogin[1])
        else:
            print("Aucun utilisateur trouvé avec ce login, veuillez saisir un login connu.")
            menu_gestion_users_bdd(cur,conn, role, site)
    elif option == 4:
        getListUser(cur, conn, role, site)
    elif option == 0:
        menu(cur, conn, role, site)
    else:
        print(f"Choix incorrect, merci de sélectionner une option.")
        menu_gestion_users_bdd(cur,conn,role, site)

    menu_gestion_users_bdd(cur, conn, role, site)

## MENU SECURITE RESEAU ##
def menu_secu_reseau(cur, conn):
    print("\n######################################")
    print("# [1] Tester les ports connus        #")
    print("# [2] Choissir une plage de ports    #")
    print("# [3] Liste des ports ouverts        #")
    print("# [0] Retour au menu principal       #")
    print("######################################\n")

    option = int(input("Choisissez une option : "))

    if option == 1:
        scanports_auto()
    elif option == 2:
        scanports_manuel()
    elif option == 3:
        print(f"Liste des ports ouverts")
    elif option == 0:
        menu(cur, conn)
    else:
        print(f"Erreur")
        menu_secu_reseau(cur,conn)

    option = int(input("Choisissez une option : "))

## MENU BOITE A OUTILS ##
def menu_tools(cur, conn):
    print("\n######################################")
    print("# [1] Sécurité des ports             #")
    print("# [2] Brute Force                    #")
    print("# [3] Liste des ports ouverts        #")
    print("# [0] Retour au menu principal       #")
    print("######################################\n")

    option = int(input("Choisissez une option : "))

    if option == 1:
        menu_secu_reseau(cur, conn)
    elif option == 2:
        print(f"Choisir plage de ports")
    elif option == 3:
        print(f"Liste des ports ouvers")
    elif option == 0:
        menu(cur, conn)
    else:
        print(f"Erreur")
        menu_tools(cur, conn)

    option = int(input("Choisissez une option : "))

## MENU FTP ##
def menu_ftp(cur,conn, role, site):
    print("\n######################################")
    print("# [1] Afficher le répertoire courant #")
    print("# [2] Choix 2                        #")
    print("# [3] Choix 3                        #")
    print("# [0] Retour au menu principal       #")
    print("######################################\n")

    option = int(input("Choisissez une option : "))

    if option == 1:
        ftp_conf()
        menu_ftp()
    elif option == 2:
        print(f"Choix 2")
    elif option == 3:
        print(f"Choix 3")
    elif option == 0:
        menu(cur,conn, role, site)
    else:
        print(f"Erreur", menu_ftp())

    option = int(input("Choisissez une option : "))
    
## MENU SUPERADMIN #
def menu(cur,conn, role, site):
    print("\n######################################")
    if(role == 1 or role == 2):
        print("# [1] Gestion des utilisateurs en BDD #")
    if(role == 1):
        print("# [2] Boite à outils                  #")
        print("# [3] Service FTP                     #")
    if(role == 3):
        print("# [1] Modifier votre mot de passe    #")
    print("# [0] Quitter le programme.          #")
    print("######################################\n")

    option = int(input("Choisissez une option : "))

    if option == 1:
        if(role == 1 or role == 2):
            menu_gestion_users_bdd(cur, conn, role, site)
        else:
            print("modification du mdp")
        pass
    elif option == 2:
        menu_secu_reseau(cur, conn)
    elif option == 3:
        menu_ftp()
    elif option == 0: 
        print("Merci d'avoir utilisé l'application teamnetway !")
        exit(0)
    else:
        print("Choix incorrect, merci de sélectionner une option.")
        menu(cur,conn, role, site)