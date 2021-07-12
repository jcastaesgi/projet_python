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

# Vérification du mot passe
mdp_stocke = hash_mdp(pwd)
print(mdp_stocke)
print(check_mdp(mdp_stocke,pwd))

if check_mdp(mdp_stocke,pwd) == True:
    print("Votre mot de passe est correct !")
else:
    print("Votre mot de passe est incorrect !")




###########################################################################################################################
# while True:
#     print("Veuillez entrer un mot de passe !")
#     password = input()
#     if re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.[@#$%^&+=])[A-Za-z0-9@#$%^&+=]{12,}$', password):
#         print("Votre mot de passe est sécurisé !")
#         break
#     else:
#         print("Votre mot de passe n'est pas assez complexe !")

###########################################################################################################################
# password=input("Veuillez entrer un mot de passe ! : ")
# if(re.match(r'^.*(?=.{12,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$', password)):
#     print("MATCH")
# else:
#     print("NOT MATCH")
###########################################################################################################################

# pwd=input("Veuillez taper un mot de passe ! : ")

# password = input("Veuillez taper votre mot de passe ! ")
# flag = 0
# while True:  
#     if (len(password)<12):
#         flag = -1
#         break
#     elif not re.search("[a-z]", password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]", password):
#         flag = -1
#         break
#     elif re.search("\s", password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break
  
# if flag ==-1:
#     print("Not a Valid Password")