import hashlib, binascii, os
import random
import string

# Listing des caractères pour le mot de passe
liste_characteres=string.ascii_letters+string.digits+string.punctuation
print("Les caractères disponibles : ",liste_characteres)
pwd=""


# Création du mot de passe à 12 charactères
for i in range(12):
    pwd+=liste_characteres[random.randint(0, len(liste_characteres)-1)]
print("Le mot de passe généré est : ",pwd)

###########################################################################################################################
# Hash du mot de passe
def hash_mdp(mdp):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    mdp_hash = hashlib.pbkdf2_hmac('sha512',mdp.encode('utf-8'),
    salt,100000)
    mdp_hash = binascii.hexlify(mdp_hash)
    return (salt+mdp_hash).decode('ascii')

# Revert du hash
def check_mdp(mdp_stocke, user_mdp):
    salt = mdp_stocke[:64]
    mdp_stocke = mdp_stocke[64:]
    mdp_hash = hashlib.pbkdf2_hmac('sha512',user_mdp.encode('utf-8'),
    salt.encode('ascii'),
    100000)
    mdp_hash = binascii.hexlify(mdp_hash).decode('ascii')
    return mdp_hash == mdp_stocke
###########################################################################################################################
# Vérification du mot passe
mdp_stocke = hash_mdp(pwd)
print(mdp_stocke)
print(check_mdp(mdp_stocke,pwd))

if check_mdp(mdp_stocke,pwd) == True:
    print("Votre mot de passe est correct !")
else:
    print("Votre mot de passe est incorrect !")
###########################################################################################################################