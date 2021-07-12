# Scan de ports auto

def scanports_auto(port):
    # Import des modules
    import pyfiglet
    import socket

    # Création de la bannière en ascii + affichage de la bannière
    banniere = pyfiglet.figlet_format("SCAN  DE  PORTS")
    print(banniere)


    bdd="127.0.0.1"
    mon_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        mon_socket.connect((bdd, port))
        return True
    except:
        return False
    mon_socket.close()


# Scan de port manuel

def scanports_manuel(port):
    # Import des modules
    import pyfiglet
    import socket

    # Création de la bannière en ascii + affichage de la bannière
    banniere = pyfiglet.figlet_format("SCAN  DE  PORTS")
    print(banniere)


    bdd="127.0.0.1"
    mon_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Liste des ports que l'on va scanner
    liste_port1=int(input("Veuillez rentrer le début de la liste de ports : "))
    liste_port2=int(input("Veuillez rentrer la fin de la liste de ports : "))+1

    for port in range (liste_port1,liste_port2): 
        if scanports_manuel(port):
            print("Le port", port, "ouvert !")
        else:
            print("Le port", port, "fermé !")
            continue