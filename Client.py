import socket

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #construction du socket
connexion_avec_serveur.connect(('localhost', 12800)) #Connecter le client au serveur

serveur_lance = True
msg_send = connexion_avec_serveur.send(b"Tu me recois ?")
msg_recu = connexion_avec_serveur.recv(1024)
print(msg_recu)

rep = b""
while serveur_lance:
    rep = input("votre message : ")
    rep = rep.encode()
    msg_send = connexion_avec_serveur.send(rep)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu)
    chaine = input("voulez vous continuer ? (O/N) :")
    if chaine == "N":
        serveur_lance = False

connexion_avec_serveur.close() #ffermerture de la connexion
