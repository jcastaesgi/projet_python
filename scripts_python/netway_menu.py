# Import des modules
from consolemenu import *
from consolemenu.items import *
import pyfiglet
import os

# Import de fichiers python
from netway_scan_port import *

def menu_superadmin():
    # CREATION DU MENU PRINCIPAL
    menu = ConsoleMenu("Menu principal", "Bienvenue dans le programme SuperAdmin de Team_Netway :")

    # CREATION DU SOUS-MENU GESTION USERS BDD
    gestion_users = SelectionMenu(["Création d'utilisateurs", "Modification d'utilisateurs", "Suppression d'utilisateurs"])
    
    # CREATION DU MENU CONTENANT LE SOUS MENU GESTION_USERS
    submenu_item_gestion_user = SubmenuItem("Gestion des utilisateurs", gestion_users, menu)
    function_item = FunctionItem("Sécurité des serveurs -PORTS-",input)

    # AFFICHAGE DES MENUS DANS MENU PRINCIPAL
    menu.append_item(submenu_item_gestion_user)
    menu.append_item(function_item)
    
    # AFFICHER LE MENU INTERACTIF
    menu.show()



def menu_admin():
    # CREATION DU MENU PRINCIPAL
    menu = ConsoleMenu("Menu principal", "Bienvenue dans le programme Utilisateur Team_Netway:")

    # CREATION DU SOUS-MENU GESTION USERS BDD
    gestion_users = SelectionMenu(["Création d'utilisateurs", "Modification d'utilisateurs", "Suppression d'utilisateurs"])

    # CREATION DU MENU CONTENANT LE SOUS MENU GESTION_USERS
    submenu_item = SubmenuItem("Gestion des utilisateurs", gestion_users, menu)

    # AFFICHAGE DES MENUS DANS MENU PRINCIPAL
    menu.append_item(submenu_item)

    # AFFICHER LE MENU INTERACTIF
    menu.show()





def menu_user():
    # CREATION DU MENU PRINCIPAL
    menu = ConsoleMenu("Menu principal", "Bienvenue dans le programme Utilisateur Team_Netway:")

    # CREATION DU SOUS-MENU GESTION USERS BDD
    gestion_users = SelectionMenu(["Création d'utilisateurs", "Modification d'utilisateurs", "Suppression d'utilisateurs"])

    # CREATION DU MENU CONTENANT LE SOUS MENU GESTION_USERS
    submenu_item = SubmenuItem("Gestion des utilisateurs", gestion_users, menu)

    # AFFICHAGE DES MENUS DANS MENU PRINCIPAL
    menu.append_item(submenu_item)

    # AFFICHER LE MENU INTERACTIF
    menu.show()