import LCD1602
from gpiozero import LED
from gpiozero import Button
import time
from time import sleep
from controleur import Controleur

def setup():
    LCD1602.init(0x27, )
    LCD1602.write(0,0, "Joueur: " + Controleur.enregistrer_donnees() )
    #LCD1602.write(1,1, "Joueur1: " + Controleur.joueur2)
    time.sleep(2)


vert = LED(12)
bleu = LED(23)
rouge = LED(20)
jaune = LED(21)

boutonV = Button(13)
boutonB = Button(4)
boutonR = Button(22)
boutonJ = Button(17)

while True:
    if boutonV.is_pressed:
        vert.on()
    else:
        vert.off()
        sleep(0.1)
    if boutonB.is_pressed:
        bleu.on()
    else:
        bleu.off()
        sleep(0.1)
    if boutonR.is_pressed:
        rouge.on()
    else:
        rouge.off()
        sleep(0.1)
    if boutonJ.is_pressed:
        jaune.on()
    else:
        jaune.off()
        sleep(0.1)