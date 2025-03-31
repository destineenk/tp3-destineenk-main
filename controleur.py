import tkinter as tk
from modele import Modele
from vue import Vue

class Controleur:
            
    #Gère les interactions entre l'utilisateur et l'application
    
    def __init__(self, fichier_json):
        self.modele = Modele(fichier_json)
        self.fenetre = tk.Tk()
        self.vue = Vue(self.fenetre)
        self.vue.set_controleur(self)
        
        #Récupère les données saisons et les enregistre dans le fichier JSON.
    def enregistrer_donnees(self):
        joueur1 = self.vue.get_nomJoueur1()
        joueur2 = self.vue.get_nomJoueur2()
        
        if joueur1 and joueur2: 
            Modele.enregistrer_donnees(joueur1, joueur2)                    
            
    def executer(self):
        #lance l'application Tkinter.
        self.fenetre.mainloop()
        
        