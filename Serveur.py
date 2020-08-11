import socket

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #construction du socket
connexion_avec_client, infos_connexion = connexion_principale.accept() #Accepter une connexion venant du client