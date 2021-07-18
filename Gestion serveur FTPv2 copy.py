### GESTION SERVEUR FTP ######

from ftplib import FTP
import ftplib
from os import chdir, getcwd
import sys, socket, glob

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
    return ftp
    return MonSocket

## Fonction pour afficher le répertoire
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
        print("Voici le contenu du répertoire ud serveur FTP : ") 
        ftp.dir()
        print("Upload OK")
        fs.close()
    except:
        print("Le fichier source n'existe pas")

## Fonction pour télécharger un fichier du serveur FTP
## Le download ne fonctionne pas encore !!!!
def Download():
    try:
        "Fichier à télécharger"
        ContenuRep_FTP()
        print("Voici le contenu du répertoire du serveur FTP : ") 
        ftp.dir()
        destination = input("Choisissez quel fichier souhaitez-vous télécharger : ")
        fichier_destination = open(destination, "wb")
        ftp.retrbinary('RETR' + destination, fichier_destination.write, 1024)
        print("Contenu de votre répertoire après download :", dir)
    except:
        print("Une erreur est survenu")


ftp = login()
Upload_FTP()
Download()

## Je dois savoir ou est-ce je dois placer la fermeture du socket, ici il ne reconnait pas la varibale "MonSocket" (ce qui est normal)

#MonSocket.close()
