import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #construction du socket
connexion_principale.bind((hote, port))#connexion au port 12800
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept() #Accepter une connexion venant du client
print(infos_connexion)