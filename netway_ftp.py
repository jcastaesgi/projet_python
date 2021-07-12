### GESTION SERVEUR FTP ######

def ftp_conf():
    from ftplib import FTP
    from os import chdir, getcwd
    import sys

    chdir("C:/users/someb/Downloads/")
    dir = getcwd()
    def Gestion_FTP():
        try:
            ## Se connecter au serveur FTP
            a = input("Entrer l'adresse IP du serveur : ")
            ftp_host = a
            ftp_login = input("Entrer votre login : ")
            ftp_password = input("Entrer votre mot de passe : ")
            ftp = FTP(ftp_host, ftp_login, ftp_password)
            print("Connection OK")
            print(ftp.getwelcome())
            ## Afficher le contenu du dossier
            print("Contenu du répertoire courant :", dir)
            ftp.dir()
        except:
            print("Connection échoué")
    Gestion_FTP()