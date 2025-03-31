import tkinter as tk

class Vue:
    #Interface utilisateur Tkinter
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("TP3 Destinée Nkodia")
        self.fenetre.geometry("350x200")
        
        
        #champ noms joueur1
        self.lbl_joueur1 = tk.Label(self.fenetre, text="Joueur1: ")
        self.lbl_joueur1.pack()
        self.ety_joueur1 = tk.Entry(self.fenetre)
        self.ety_joueur1.pack()
        
        #label affichage pts joueur1
        self.lbl_pts1 = tk.Label(self.fenetre, text="")
        self.lbl_pts1.pack()
        
        #champ noms joueur2
        self.lbl_joueur2 = tk.Label(self.fenetre, text="Joueur2: ")
        self.lbl_joueur2.pack()
        self.ety_joueur2 = tk.Entry(self.fenetre)
        self.ety_joueur2.pack()
        
        #label affichage pts joueur2
        self.lbl_pts2 = tk.Label(self.fenetre, text="")
        self.lbl_pts2.pack()
        
        #bouton valider
        self.btn_valider = tk.Button(self.fenetre, text="Valider", command= None)
        self.btn_valider.pack(pady=10)
        
        #bouton débuter
        self.btn_debut = tk.Button(self.fenetre, text="Début de partie")
        self.btn_debut.pack(pady=10)
        
        #affichage question
        self.affichageQuestion = tk.Text(self.fenetre)
        self.affichageQuestion.config(state = tk.DISABLED) #lecture seule
        self.affichageQuestion.pack()
        
        
        #bouton recommencer
        self.btn_recommencer = tk.Button(self.fenetre, text="Recommencer une partie", command= None)
        self.btn_recommencer.pack(pady=10)
    
    def set_controleur(self, controleur):
        #Associe le bouton au contrôleur, Événement
        self.btn_valider.config(command=controleur.enregistrer_donnees)
        
    def get_nomJoueur1(self): #recupère nom du joueur1 saisi
        return self.ety_joueur1.get()
    
    def get_nomJoueur2(self): #Récupère nom du joueur2
        return self.ety_joueur2.get()
    
    def affichage_ptsJoueur1(self, points1):
        #affichages les pts du joueur1
        return self.lbl_pts1.config(text=points1)
        
    def affichage_ptsJoueur1(self, points2):
        #affichages les pts du joueur1
        self.lbl_pts1.config(text=points2)
        
    def affichageQuestionnaire(self, questions):
        #affichage questions et choix 
        return self.affichageQuestion.config(text = questions)
        
        
        
        
        
        