### GESTION SERVEUR FTP ######

from ftplib import FTP
import ftplib
import sys, socket, glob, os
from os import chdir, getcwd

## Fonction connection au serveur avec socket
def login():
    try:
        "Se connecter au serveur FTP"
        ftp_host = input("Entrer l'adresse IP du serveur : ")
        ftp_login = input("Entrer votre login : ")
        ftp_password = input("Entrer votre mot de passe : ")
        MonSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        MonSocket.connect((ftp_host,14147))
        ftp = FTP(ftp_host, ftp_login, ftp_password)
        print("Connection OK")
        print(ftp.getwelcome())
    except:
        print("Connection échoué")
        MonSocket.close()

    return ftp
    return MonSocket

## Fonction pour se placer dans le répertoire auquel nous souhaitons travailler, (utilisé pour le Upload et le Download)
def ContenuRep_FTP():
    print("Vous devez connaitre le chemin exact de votre répertoire")
    local = input("Entrer votre répertoire de travail : ")
    chdir(local)
    dir = glob.glob("*")
    try:
        "Afficher le contenu du dossier"
        print("Contenu du répertoire courant :", dir)
    except:
        print("Répertoire inexistant")

## Fonction pour envoyer un fichier au serveur FTP
def Upload_FTP():
    ContenuRep_FTP()
    try:
        "Fichier à envoyer"
        fichier = input("Quel fichier ou répertoire souhaitez-vous envoyer depuis la liste ci-dessus ? ")
        fs = open(fichier, "rb")
        ftp.storbinary('STOR '+fichier, fs)
        print("Voici le contenu du répertoire du serveur FTP : ") 
        ftp.dir()
        print("Upload OK")
        fs.close()
    except:
        print("Le fichier source n'existe pas")

## Fonction pour télécharger un fichier du serveur FTP
## Le download n'a pas été testé encore !!!
def Download():
    ContenuRep_FTP()
    try:
        "Fichier à télécharger"
        print("Voici le contenu du répertoire du serveur FTP : ") 
        dirftp = ftp.dir()
        try:
            ds = input("Dans quel répertoire souhaitez vous vous placer ? : ")
            ftp.cwd(ds)
            print("Voici les dossiers actuels")
            dirftp = ftp.dir()
            choix = input("Souhaitez-vous déplacer dans un sous-répertoire (y/n) ? ")
            while choix == "y":
                ds = input("Dans quel répertoire souhaitez vous vous placer ? : ")
                ftp.cwd(ds)
                print("Voici les dossiers actuels")
                dirftp = ftp.dir()
            else:
                continue
        except:
            print("Le répertoire n'existe pas")
            sys.exit()
        destination = input("Choisissez quel fichier souhaitez-vous télécharger : ")
        fichier_destination = open(destination, "wb")
        ftp.retrbinary('RETR' + destination, fichier_destination.write, 1024)
        print("Contenu de votre répertoire après download :", dir)
    except:
        print("Une erreur est survenu")

## Fonction création de répertoire
def create_dir():
    " Choix du répertoire dans lequel ce déplacer"
    print("Voici votre répertoire actuel")
    dirftp = ftp.dir()
    try:
        ds = input("Dans quel répertoire souhaitez vous vous placer ? : ")
        ftp.cwd(ds)
        print("Voici les dossiers actuels")
        dirftp = ftp.dir()
    except:
        print("Répertoire inexistant")
        sys.exit()
    "Création de répertoire"
    dossier = input("Entrer le nom du répertoire a créer : ")
    if dossier is dirftp: ## Le code ne rentre pas dans le if si le répertoire existe, il me sort donc une erreur comme quoi le dossier existe déja
        print("Le répertoire existe déja")
        create_dir()
    else:
        print("Création du répertoire en cours... ")
        ftp.mkd(dossier)
        print("répertoire", dossier, "crée")
    
## Fonction suppression de fichier ou répertoire
def remove():
    "Suppression de répertoire"
    print("Voici votre répertoire actuel")
    dirftp = ftp.dir()
    choix = input("Souhaitez-vous déplacer dans un sous-répertoire (y/n) ? ")
    if choix != "y":
        sup = input("Quel fichier ou dossier souhaitez-vous supprimer ? ")
        if "." in sup:
            ftp.delete(sup)
            print("Le fichier", sup, "a été supprimé")
        else:
            ftp.rmd(sup)
            print("Le dossier", sup, "a été supprimé")
    else:
        ds = input("Dans quel répertoire souhaitez vous vous placer ? : ")
        ftp.cwd(ds)
        remove()
        
     

ftp = login()
#create_dir()
#remove()
#Upload_FTP()
#Download()
