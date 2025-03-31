import json, codecs

class Modele:
    
    #Gérer les données et les interactions avec le fichier JSON.
    def __init__(self,fichier):
        self.fichier = fichier
        
    def enregistrer_donnees(self, joueur1, joueur2):
        #enregistre les données du joueur 1
        nouvelles_donnes = {"joueur1": joueur1, "joueur2": joueur2}
        
        try:
            with codecs.open(self.fichier, "r", encoding="utf-8") as f:
                donnees = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            donnees = [] #Crée une liste vide si le fichier n'existe pas ou est corrompu
            
        donnees.append(nouvelles_donnes)   # ajoute les nouvelles données
        
        with codecs.open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=4, ensure_ascii = False) #Sauvegarde des données
            
            
    