import socket

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #construction du socket
connexion_avec_serveur.connect(('localhost', 12800)) #Connecter le client au serveur

