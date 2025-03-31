from controleur import Controleur

if __name__ == "__main__":
    FICHIER_JSON = "donnees.json" #Fichier de sauvegarde json
    app = Controleur(FICHIER_JSON)
    app.executer()
