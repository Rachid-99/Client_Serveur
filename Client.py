import socket

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #construction du socket
connexion_avec_serveur.connect(('localhost', 12800)) #Connecter le client au serveur

msg_recu = connexion_avec_serveur.recv(1024)
print(msg_recu)

connexion_avec_serveur.close() #ffermerture de la connexion
