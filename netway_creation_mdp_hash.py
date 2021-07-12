import hashlib, binascii, os
import re

# Demande de renter un mot de passe
while True:
    pwd = input("Veuillez entrer un mot de passe ! :")
# Vérification des prérequis pour le mot de passe avec un regex
    if re.fullmatch(r'^.*(?=.{12,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$', pwd): 
        print("Votre mot de passe est sécurisé !")
        break
    else:
        print("Votre mot de passe n'est pas assez complexe !")
###########################################################################################################################
# Hash du mot de passe
def hash_mdp(mdp):
# hexdigest : converti la chaine de caractère en hexa 
# Salt : Sel pour le hashage randomisé jusqu'à 16 octets
# os.random : calcul le premier hash avec le random
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii') 
#pbkdf2_hmac : permet de choisir le type de hash                                
    mdp_hash = hashlib.pbkdf2_hmac('sha512',mdp.encode('utf-8'), 
# 100000 : nombre d'itération de sha256
    salt,100000)
    mdp_hash = binascii.hexlify(mdp_hash)
    return (salt+mdp_hash).decode('ascii')

# Comparaison de l'empreinte du hash avec le mot de passe
def check_mdp(mdp_stocke, user_mdp):
    salt = mdp_stocke[:64] # 64 octets = Taille de la clé
    mdp_stocke = mdp_stocke[64:]
    mdp_hash = hashlib.pbkdf2_hmac('sha512',user_mdp.encode('utf-8'), 
    salt.encode('ascii'),
    100000)
    mdp_hash = binascii.hexlify(mdp_hash).decode('ascii')
    return mdp_hash == mdp_stocke

# # Vérification du mot passe
mdp_stocke = hash_mdp(pwd)
print(mdp_stocke)
print(check_mdp(mdp_stocke,pwd))

if check_mdp(mdp_stocke,pwd):
    print("Votre mot de passe est correct !")
else:
    print("Votre mot de passe est incorrect !")
###########################################################################################################################