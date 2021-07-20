                                        ############# GESTION SERVEUR FTP ###########

from ftplib import FTP
import ftplib
import sys, socket, glob, os
from os import chdir, getcwd

############# Fonction connection au serveur avec socket ###########
def login():
    try:
        "Se connecter au serveur FTP"
        ftp_host = input("Entrer l'adresse IP du serveur : ")
        ftp_login = input("Entrer votre login : ")
        ftp_password = input("Entrer votre mot de passe : ")
        MonSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        MonSocket.connect((ftp_host,14147))
        ftp = FTP(ftp_host, ftp_login, ftp_password)
        print("      ___           ___                       ___           ___                 ")
        print("     /__/\         /  /\          ___        /__/\         /  /\          ___   ")
        print("     \  \:\       /  /:/_        /  /\      _\_ \:\       /  /::\        /__/|  ")
        print("      \  \:\     /  /:/ /\      /  /:/     /__/\ \:\     /  /:/\:\      |  |:|  ")
        print("  _____\__\:\   /  /:/ /:/_    /  /:/     _\_ \:\ \:\   /  /:/~/::\     |  |:|  ")
        print(" /__/::::::::\ /__/:/ /:/ /\  /  /::\    /__/\ \:\ \:\ /__/:/ /:/\:\  __|__|:|  ")
        print(" \  \:\~~\~~\/ \  \:\/:/ /:/ /__/:/\:\   \  \:\ \:\/:/ \  \:\/:/__\/ /__/::::\  ")
        print("  \  \:\  ~~~   \  \::/ /:/  \__\/  \:\   \  \:\ \::/   \  \::/         ~\~~\:\ ")
        print("   \  \:\        \  \:\/:/        \  \:\   \  \:\/:/     \  \:\           \  \:\"")
        print("    \  \:\        \  \::/          \__\/    \  \::/       \  \:\           \__\/")
        print("     \__\/         \__\/                     \__\/         \__\/                ")

        print(ftp.getwelcome())
    except:
        print("Connection échoué")
        MonSocket.close()

    return ftp
    return MonSocket

########### Fonction pour se placer dans le répertoire auquel nous souhaitons travailler, (utilisé pour le Upload et le Download) ###########
def ContenuRep_FTP():
    print("Vous devez connaitre le chemin exact de votre répertoire \n  - Pour le Download placé vous dans le répertoire auquel vous souhaitez déposer le fichier \n  - Pour le Upload placé vous dans le répertoire où ce trouve le fichier à envoyer")
    local = input("Entrer votre répertoire de travail : ")
    chdir(local)
    dir = glob.glob("*")
    try:
        "Afficher le contenu du dossier"
        print("Contenu du répertoire courant :", dir)
    except:
        print("Répertoire inexistant")
    return dir, local

############ Fonction pour envoyer un fichier au serveur FTP ###########
def Upload_FTP():
    ContenuRep_FTP()
    try:
        "Fichier à envoyer"
        fichier = input("Quel fichier ou répertoire souhaitez-vous envoyer depuis la liste ci-dessus ? ")
        dirftp = ftp.nlst()
        print(dirftp)
        ds = input("Dans quel répertoire souhaitez vous vous placer pour l'upload ? : ")
        count = 0
        for i in dirftp:
            if i == ds:
                ftp.cwd(ds)
                print("Voici les fichiers/dossiers actuels")
                dirftp = ftp.nlst()
                print(dirftp)
                count = 1
                break
        if count == 0:
            print("Le répertoire demandé n'existe pas, vous restez dans le même répertoire")
            pass
        choix = input("Souhaitez-vous déplacer dans un sous-répertoire (y/n) ? ")
        while choix == "y":
            ds = input("Dans quel répertoire souhaitez vous vous placer pour l'upload ? : ")
            count2 = 0
            for e in dirftp:
                while e == ds:
                    ftp.cwd(ds)
                    print("Voici les fichiers/dossiers actuels")
                    dirftp = ftp.nlst()
                    print(dirftp)
                    count2 = 1
                    break
            if count2 == 0:
                print("Le répertoire demandé n'existe pas")
                break
        fs = open(fichier, "rb")
        ftp.storbinary('STOR '+fichier, fs)
        print("Voici le contenu du répertoire du serveur FTP après Upload : ") 
        ftp.dir()
        print("Upload OK")
        fs.close()
    except:
        print("Le fichier source n'existe pas")

############### Fonction pour télécharger un fichier du serveur FTP ###########
def Download():
    "Fichier à télécharger"
    print("Voici le contenu du répertoire du serveur FTP : ") 
    dirftp = ftp.nlst()
    print(dirftp)
    ds = input("Dans quel répertoire souhaitez vous vous placer ? : ")
    count = 0
    for i in dirftp:
        if i == ds:
            ftp.cwd(ds)
            print("Voici les fichiers/dossiers actuels")
            dirftp = ftp.nlst()
            print(dirftp)
            count = 1
            break
    if count == 0:
        print("Le répertoire demandé n'existe pas, vous restez dans le même répertoire")
        pass
    choix = input("Souhaitez-vous déplacer dans un sous-répertoire (y/n) ? ")
    while choix == "y":
        ds = input("Dans quel répertoire souhaitez vous vous placer ? : ")
        count2 = 0
        for e in dirftp:
            while e == ds:
                ftp.cwd(ds)
                print("Voici les fichiers/dossiers actuels")
                dirftp = ftp.nlst()
                print(dirftp)
                count2 = 1
                break
        if count2 == 0:
            print("Le répertoire demandé n'existe pas")
            break
    else:
        pass
    destination = input("Choisissez quel fichier souhaitez-vous télécharger : ")
    count3 = 0
    for d in dirftp:
        while d == destination:
            print("Fichier", destination, "téléchargé")
            count3 = 1
            break
    if count3 == 0:
        print("Le fichier que vous souhaitez télécharger n'existe pas")
        return
    dir, local = ContenuRep_FTP()
    fichier_destination = open(destination, "wb")
    ftp.retrbinary('RETR '+ destination, fichier_destination.write, 1024)
    print("Contenu de votre répertoire après dépôt du fichier")
    chdir(local)
    dir = glob.glob("*")
    print(dir)
    fichier_destination.close()

######### Fonction création de répertoire ###########
def create_dir():
    " Choix du répertoire dans lequel ce déplacer"
    print("Voici votre répertoire actuel")
    dirftp = ftp.nlst()
    print(dirftp)
    try:
        ds = input("Dans quel répertoire souhaitez vous vous placer ? : ")
        ftp.cwd(ds)
        print("Voici les dossiers actuels")
        dirftp = ftp.nlst()
        print(dirftp)
    except:
        print("Répertoire inexistant")
        sys.exit()
    "Création de répertoire"
    dossier = input("Entrer le nom du répertoire a créer : ")
    cont=0
    for r in dirftp:
        while r == dossier:
            print("Le répertoire existe déja")
            cont=1
            break
    if cont==0:
        print("Création du répertoire en cours... ")
        ftp.mkd(dossier)
        print("répertoire", dossier, "crée")
        return
        
    
########## Fonction suppression de fichier ou répertoire ###########
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
            print(dirftp)
        else:
            ftp.rmd(sup)
            print("Le dossier", sup, "a été supprimé")
            print(dirftp)
    else:
        ds = input("Dans quel répertoire souhaitez vous vous placer ? : ")
        ftp.cwd(ds)
        remove()

######## Fonction consultation de fichier ###########
def consult_dir():
    "Consultation de répertoire"
    print("Voici votre home directory sur le serveur FTP")
    home_directory = ftp.nlst()
    directory = home_directory
    print(home_directory)
    choix = input("Souhaitez-vous consulter un sous-répertoire ? (y/n) : ")
    while choix == "y":
        ds = input("Quel répertoire souhaitez-vous consulter : ")
        count4 = 0
        for c in directory:
            while c == ds:
                ftp.cwd(ds)
                print("Voici les fichiers/dossiers actuels")
                directory = ftp.nlst()
                print(directory)
                count4 = 1
                break
        if count4 == 0:
            print("Le dossier que vous souhaitez consulter n'existe pas")
            break
    else:
        print("Fin du programme")
        sys.exit()


ftp = login()
#create_dir()
#remove()
Upload_FTP()
#Download() 
#consult_dir()
