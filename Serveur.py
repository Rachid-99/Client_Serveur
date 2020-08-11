import socket
import select

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #construction du socket
connexion_principale.bind((hote, port))#connexion au port 12800
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))
"""connexion_avec_client, infos_connexion = connexion_principale.accept() #Accepter une connexion venant du client
print(infos_connexion)
connexion_avec_client.send(b"Je viens d'accepter la connexion") #on envoie un message au client"""

serveur_lance = True
clients_connectes = [] #la liste des clients connectes au serveur

while serveur_lance:
    # On va vérifier que de nouveaux clients ne demandent pas à se connecter
    # Pour cela, on écoute la connexion_principale en lecture
    # On attend maximum 50ms
    connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()#on recupere les informations de chaque clients
        clients_connectes.append(connexion_avec_client)# On ajoute le socket connecté à la liste des clients

    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus
    # On attend là encore 50ms maximum
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
    except select.error:
        pass
    else:
        for client in clients_a_lire: # On parcourt la liste des clients à lire
            msg_recu = client.recv(1024) # Client est de type socket
            msg_recu = msg_recu.decode()
            print("Reçu : {}".format(msg_recu))
            try:
                client.send(b"5 / 5")
            except BrokenPipeError:
                pass
            if msg_recu == "fin":
                serveur_lance = False

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()