### appel des librairies ###

from tkinter import *  # pour l'interface graphique
import random  # pour générer aléatoirement des positions (départ, obstacles) 
import time  # pour faire des pause

### variables modifiables ###

vi = 2  # vitesse du jeu en général
taille = 14  # taille du personnage
co = "b"  # direction de départ

### déclarations des variables ###

difficulté = 8  # variable de la diffucultée
p = 0  # variable "pause"
ob = []  # liste contenant les coordonnées des obstacles
x1, y1 = 0, 0  # position du personnage
x2, y2 = 0, 0  # position du futur obstacle
xd, yd = 0, 0  # position du départ
xa, ya = 0, 0  # position de l'arrivée
xp, yp = 0, 0  # position du projectile
projec = 0  # variable du projectile
en = 0  # variable pour le changement de difficultée

vi = vi / 10000

### déclarations des fonctions ###

def bind(): # attribuer les différentes fonctions aux touches
    global fen
    unbind()
    fen.bind("<Left>", depl_gauche)
    fen.bind("<Right>", depl_droite)
    fen.bind("<Up>", depl_haut)
    fen.bind("<Down>", depl_bas)
    fen.bind("<space>", saut)
    fen.bind("<a>", tir)

def unbind(): # désatribuer les touches
    global fen
    fen.unbind("<Left>")
    fen.unbind("<Right>")
    fen.unbind("<Up>")
    fen.unbind("<Down>")
    fen.unbind("<space>")
    fen.unbind("<a>")

def avance(gd, hb): # faire avancer le personnage
    global x1, y1, oval, taille, vi
    x1, y1 = x1 +gd, y1 +hb
    can.delete(oval)
    oval = can.create_oval(x1-taille, y1-taille, x1+taille, y1+taille, fill="#3C787E", outline="#3C787E")
    can.update_idletasks()
    time.sleep(vi*20)

def avancep(XP, YP, X, Y): # faire avancer le projectile (lazer)
    global xp, yp, projec, vi, xp1, yp1
    xp = xp + XP
    yp = yp + YP
    xp1 = xp1 + X
    yp1 = yp1 + Y
    can.coords(projec, xp1, yp1, xp, yp)
    can.update_idletasks()

def obstacle(x): # générer des obstacles
    global difficulté, vi, can, p
    i = 0
    if p == 0 :
        for i in range (0,difficulté) :
            if len(ob) < 599:
                x2 = random.randint(0,29)*30+15
                y2 = random.randint(0,19)*30+15
                while x2 == x1 and y2 == y1 or str(x2)+str(y2) in ob:
                    x2 = random.randint(0,29)*30+15
                    y2 = random.randint(0,19)*30+15
                carre(x2, y2, x/50)

def carre(x, y, v): # faire apparraitre des carrés
    global can, vi, ob
    i = 1
    obst = can.create_rectangle(x, y, x, y, fill="#241623", outline="#241623")
    ob.append(str(x)+str(y))
    while i <= 15:
        can.coords(obst, x-i, y-i, x+i, y+i)
        can.update_idletasks()
        time.sleep(vi*v)
        i = i + 1

def défaite(): # vérifié si on a perdu
    global p, bou, fen, can, bou_win, x1, y1, xa, ya, oval, vi, taille, pe
    qx, qy = 0, 0
    if str(x1)+str(y1) in ob :

        if x1 == xa and y1 == ya :
            p = p

        else :
        
            if x1 == 885 :
                qx = -20
        
            if x1 == 15 :
                qx = 20
        
            if p == 0 :
                i = taille
                while i > 0 :
                    can.coords(oval, x1-i, y1-i, x1+i, y1+i)
                    i = i - 1
                    can.update_idletasks()
                    time.sleep(vi*250)
                time.sleep(0.1)
                bou = Button(fen, text="PERDU !", command=re, bg ="#D56F3E", fg="#241623", cursor="hand1", highlightbackground="#241623", activebackground="#D56F3E")
                bou_win = can.create_window(x1 + qx, y1 + qy, window=bou)
            p = -1
      
def victoire(): # vérifier si on a gagné
    global p, bou, fen, can, bou_win, x1, y1
    qx, qy = 0, 0
    if x1 == xa and y1 == ya:

        if ya == 15 :
            qy = 30
        else :
            qy = -30

        if xa == 885 :
            qx = -20
        
        if xa == 15 :
            qx = 20
        if p == 0 :
            bou = Button(fen, text="GAGNÉ !", command=re, bg ="#C7EF00", fg="#241623", cursor="hand1", highlightbackground="#241623", activebackground="#C7EF00")
            bou_win = can.create_window(x1 + qx, y1 + qy, window=bou)
        p = 1

def depl_gauche(event): # générer le déplacement du personnage vers la gauche
    global p, co, taille
    unbind()
    co = "g"
    i = 0
    if p == 0 and x1 > 15 :
        taille = taille + 1
        while i < 30 :
            avance(-1, 0)
            i = i + 1
        taille = taille - 1
        avance(0, 0)
        défaite()
        victoire()
        obstacle(3)
    fen.after_idle(bind)
    
def depl_droite(event): # générer le déplacement du personnage vers la droite
    global p, co, taille
    unbind()
    co = "d"
    i = 0
    if p == 0 and x1 < 885 :
        taille = taille + 1
        while i < 30 :
            avance(1, 0)
            i = i + 1
        taille = taille - 1
        avance(0, 0)
        défaite()
        victoire()
        obstacle(3)
    fen.after_idle(bind)
    
def depl_haut(event): # générer le déplacement du personnage vers le haut
    global p, co, taille
    unbind()
    co = "h"
    i = 0
    if p == 0 and y1 > 15 :
        taille = taille + 1
        while i < 30 :
            avance(0, -1)
            i = i + 1
        taille = taille - 1
        avance(0, 0)
        défaite()
        victoire()
        obstacle(3)
    fen.after_idle(bind)
    
def depl_bas(event): # générer le déplacement du personnage vers le bas
    global p, co, taille
    unbind()
    co = "b"
    i = 0
    if p == 0 and y1 < 585 :
        taille = taille + 1
        while i < 30 :
            avance(0, 1)
            i = i + 1
        taille = taille - 1
        avance(0, 0)
        défaite()
        victoire()
        obstacle(3)
    fen.after_idle(bind)
    
def saut(event): # générer le saut du personnage
    global p, co, taille
    unbind()
    i = 0
    if p == 0 :
        if co == "g" and x1 > 45 :
            while i < 30 :
                avance(-1, 0)
                taille = taille + 0.5
                i = i + 1
            while i < 60 :
                avance(-1, 0)
                taille = taille - 0.5
                i = i + 1
            défaite()
            victoire()
        if co == "d" and x1 < 855 :
            while i < 30 :
                avance(1, 0)
                taille = taille + 0.5
                i = i + 1
            while i < 60 :
                avance(1, 0)
                taille = taille - 0.5
                i = i + 1
            défaite()
            victoire()
        if co == "h" and y1 > 45 :
            while i < 30 :
                avance(0, -1)
                taille = taille + 0.5
                i = i + 1
            while i < 60 :
                avance(0, -1)
                taille = taille - 0.5
                i = i + 1
            défaite()
            victoire()
        if co == "b" and y1 < 555 :
            while i < 30 :
                avance(0, 1)
                taille = taille + 0.5
                i = i + 1
            while i < 60 :
                avance(0, 1)
                taille = taille - 0.5
                i = i + 1
            défaite()
            victoire()
        obstacle(3)
        obstacle(3)
        obstacle(3)
        taille = int(taille)
    fen.after_idle(bind)

def tir(event): # générer le tir
    global co, p, xp, yp, projec, can, fen, xp1, yp1, vi, rect1, rect2, taille
    unbind()
    i = 0
    if p == 0:
        xp, yp = x1, y1
        if co == "g" :
            xp1 = xp - taille
            xp = xp - (taille + 1)
            yp1 = yp - 2
            yp = yp + 2
            projec = can.create_rectangle(xp1, yp1, xp, yp, fill="#D56F3E", outline="#D56F3E")
            while i == 0:
                avancep(-1, 0, 0, 0)
                if str(xp)+str(yp-2) in ob :
                    yp1 = yp1 + 1
                    yp = yp - 1
                    time.sleep(vi*300)
                    can.coords(projec, xp1, yp1, xp, yp)
                    can.update_idletasks()
                    yp1 = yp1 + 1
                    yp = yp - 1
                    rect1 = can.create_rectangle(xp, yp, xp, yp, fill="Red", outline="Red")
                    rect2 = can.create_rectangle(xp, yp, xp, yp, fill="#D0CD94", outline="#D0CD94")
                    can.delete(projec)
                    projec = can.create_rectangle(xp1, yp1, xp, yp, fill="#D56F3E", outline="#D56F3E")
                    rec(xp, yp, 1, 0)
                    can.coords(projec, xp1, yp, xp, yp)
                    can.update_idletasks()
                    time.sleep(vi*300)
                    can.delete(projec)
                    ob.remove(str(xp)+str(yp))
                    i = 1
                if xp < 0 :
                    yp1 = yp1 + 1
                    yp = yp - 1
                    time.sleep(vi*300)
                    can.coords(projec, xp1, yp, xp, yp)
                    can.update_idletasks()
                    yp1 = yp1 + 1
                    yp = yp - 1
                    can.coords(projec, xp1, yp, xp, yp)
                    can.update_idletasks()
                    time.sleep(vi*900)
                    can.delete(projec)
                    i = 1
        if co == "d" :
            xp1 = xp + taille
            xp = xp + taille + 1
            yp1 = yp - 2
            yp = yp + 2
            projec = can.create_rectangle(xp1, yp1, xp, yp, fill="#D56F3E", outline="#D56F3E")
            while i == 0:
                avancep(1, 0, 0, 0)
                if str(xp)+str(yp-2) in ob :
                    yp1 = yp1 + 1
                    yp = yp - 1
                    time.sleep(vi*300)
                    can.coords(projec, xp1, yp1, xp, yp)
                    can.update_idletasks()
                    yp1 = yp1 + 1
                    yp = yp - 1
                    rect1 = can.create_rectangle(xp, yp, xp, yp, fill="Red", outline="Red")
                    rect2 = can.create_rectangle(xp, yp, xp, yp, fill="#D0CD94", outline="#D0CD94")
                    can.delete(projec)
                    projec = can.create_rectangle(xp1, yp1, xp, yp, fill="#D56F3E", outline="#D56F3E")
                    rec(xp, yp, -1, 0)
                    can.coords(projec, xp1, yp, xp, yp)
                    can.update_idletasks()
                    time.sleep(vi*300)
                    can.delete(projec)
                    ob.remove(str(xp)+str(yp))
                    i = 1
                if xp > 900 :
                    yp1 = yp1 + 1
                    yp = yp - 1
                    time.sleep(vi*300)
                    can.coords(projec, xp1, yp, xp, yp)
                    can.update_idletasks()
                    yp1 = yp1 + 1
                    yp = yp - 1
                    can.coords(projec, xp1, yp, xp, yp)
                    can.update_idletasks()
                    time.sleep(vi*900)
                    can.delete(projec)
                    i = 1
        if co == "h" :
            xp1 = xp - 2
            xp = xp + 2
            yp1 = yp - taille
            yp = yp - (taille + 1)
            projec = can.create_rectangle(xp1, yp1, xp, yp, fill="#D56F3E", outline="#D56F3E")
            while i == 0:
                avancep(0, -1, 0, 0)
                if str(xp-2)+str(yp) in ob :
                    xp1 = xp1 + 1
                    xp = xp - 1
                    time.sleep(vi*300)
                    can.coords(projec, xp1, yp1, xp, yp)
                    can.update_idletasks()
                    xp1 = xp1 + 1
                    xp = xp - 1
                    rect1 = can.create_rectangle(xp, yp, xp, yp, fill="Red", outline="Red")
                    rect2 = can.create_rectangle(xp, yp, xp, yp, fill="#D0CD94", outline="#D0CD94")
                    can.delete(projec)
                    projec = can.create_rectangle(xp1, yp1, xp, yp, fill="#D56F3E", outline="#D56F3E")
                    rec(xp, yp, 0, 1)
                    can.coords(projec, xp1, yp1, xp, yp)
                    can.update_idletasks()
                    time.sleep(vi*300)
                    can.delete(projec)
                    ob.remove(str(xp)+str(yp))
                    i = 1
                if yp <= 0 :
                    xp1 = xp1 + 1
                    xp = xp - 1
                    time.sleep(vi*300)
                    can.coords(projec, xp1, yp1, xp, yp)
                    can.update_idletasks()
                    xp1 = xp1 + 1
                    xp = xp - 1
                    can.coords(projec, xp1, yp1, xp, yp)
                    can.update_idletasks()
                    time.sleep(vi*900)
                    can.delete(projec)
                    i = 1
        if co == "b" :
            xp1 = xp - 2
            xp = xp + 2
            yp1 = yp + taille
            yp = yp + taille + 1
            projec = can.create_rectangle(xp1, yp1, xp, yp, fill="#D56F3E", outline="#D56F3E")
            while i == 0:
                avancep(0, 1, 0, 0)
                if str(xp-2)+str(yp) in ob :
                    xp1 = xp1 + 1
                    xp = xp - 1
                    time.sleep(vi*300)
                    can.coords(projec, xp1+2, yp1, xp, yp)
                    can.update_idletasks()
                    xp1 = xp1 + 1
                    xp = xp - 1
                    rect1 = can.create_rectangle(xp, yp, xp, yp, fill="Red", outline="Red")
                    rect2 = can.create_rectangle(xp, yp, xp, yp, fill="#D0CD94", outline="#D0CD94")
                    can.delete(projec)
                    projec = can.create_rectangle(xp1, yp1, xp, yp, fill="#D56F3E", outline="#D56F3E")
                    rec(xp, yp, 0, -1)
                    can.coords(projec, xp, yp1, xp, yp)
                    can.update_idletasks()
                    time.sleep(vi*300)
                    can.delete(projec)
                    projec = 0
                    ob.remove(str(xp)+str(yp))
                    i = 1
                if yp >= 600 :
                    xp1 = xp1 + 1
                    xp = xp - 1
                    time.sleep(vi*300)
                    can.coords(projec, xp1+2, yp1, xp, yp1)
                    can.update_idletasks()
                    xp1 = xp1 + 1
                    xp = xp - 1
                    can.coords(projec, xp, yp1, xp, yp)
                    can.update_idletasks()
                    time.sleep(vi*900)
                    can.delete(projec)
                    i = 1
    défaite()
    victoire()
    obstacle(3)
    obstacle(3)
    fen.after_idle(bind)

def rec(xp, yp, x, y): # faire péter l'obstacle
    global fen, can, vi, rect1, rect2, x1, y1
    i = 1
    if x1 <= 15 or x1 >= 885 :
        x = 0
    if y1 <= 15 or y1 >= 585 :
        y = 0
    avance(x, y)
    avancep(0, 0, x, y)
    while i <= 14:
        can.coords(rect1, xp-i, yp-i, xp+i, yp+i)
        avance(x, y)
        avancep(0, 0, x, y)
        i = i + 1
        can.update_idletasks()
        time.sleep(vi*75)
    i = 1
    while i <= 14:
        can.coords(rect2, xp-i, yp-i, xp+i, yp+i)
        avance(x, y)
        avancep(0, 0, x, y)
        i = i + 1
        can.update_idletasks()
        time.sleep(vi*75)
    avance(x, y)
    avancep(0, 0, x, y)

def canv(): # générer la zone de jeu
    global xd, yd, xa, ya, x1, y1, can, fen, oval, bout, entree, difficulté, p, ob, la, la2, en, xp, yp, projec, co, taille, boutc, la3, vi
    p = 0
    ob = []
    en = int(entree.get())
    difficulté = en
    bout.destroy()
    boutc.destroy()
    entree.destroy()
    la.destroy()
    la2.destroy()
    la3.destroy()
    
    fen.title("Squared Blockers, level " + str(difficulté))
    can = Canvas(fen,bg="#D0CD94",height=600,width=900)
    can.pack()

    xd = random.randint(0,29)*30+15
    yd = random.randint(0,19)*30+15
    while xd > 175 and xd < 735 or xd < 75 or xd > 835 :
        xd = random.randint(0,29)*30+15
    while yd > 525 or yd < 75 :
        yd = random.randint(0,19)*30+15
    de = can.create_rectangle(xd-15, yd-15, xd+15, yd+15, fill="#D56F3E", outline="#D56F3E")
    i = 0
    while i <= 15:
        can.coords(de, xd-i, yd-i, xd+i, yd+i)
        i = i + 1
        can.update_idletasks()
        time.sleep(vi*100)
    ob.append(str(xd)+str(yd))
    x1, y1 = xd, yd

    xa = random.randint(0,29)*30+15
    ya = random.randint(0,19)*30+15
    if xd <= 175 and xd >= 75 :
        while xa > 835 or xa < 735 :
            xa = random.randint(0,29)*30+15
        while ya > 525 or ya < 75 :
            ya = random.randint(0,19)*30+15
    if xd >= 735 and xd <= 835 :
        while xa < 75 or xa > 175 :
            xa = random.randint(0,29)*30+15
        while ya > 525 or ya < 75 :
            ya = random.randint(0,19)*30+15
    
    ar = can.create_rectangle(xa-15, ya-15, xa+15, ya+15, fill="#C7EF00", outline="#C7EF00")
    i = 0
    while i <= 15:
        can.coords(ar, xa-i, ya-i, xa+i, ya+i)
        i = i + 1
        can.update_idletasks()
        time.sleep(vi*100)
    ob.append(str(xa)+str(ya))

    i = 0
    oval = can.create_oval(x1-taille, y1-taille, x1+taille, y1+taille, fill="#3C787E", outline="#3C787E")
    while i <= taille :
        can.coords(oval, x1-i, y1-i, x1+i, y1+i)
        i = i + 1
        can.update_idletasks()
        time.sleep(vi*100)
    
    time.sleep(1)
    
    for i in range (0, 100//difficulté):
        obstacle(2)
    
    fen.after_idle(bind)

    
def re(): # réafficher le menu de sélection
    global fen, can, bou, bout, entree, p, la, la2, en, boutc, la3
    unbind()
    p = int(p)
    en = int(en)
    can.destroy()
    fen.title("Squared Blockers")
    bout = Button(fen, command=canv, text="--> Jouer <--", bg="#D0CD94", fg="#241623", cursor="hand1", highlightbackground="#D0CD94", activebackground="#3C787E")
    boutc = Button(fen, command=credi, text="Crédits (niveau spécial!)", bg="#D0CD94", fg="#241623", cursor="hand1", highlightbackground="#D0CD94", activebackground="#241623", activeforeground="#D0CD94")
    entree = Spinbox(fen, from_=1, to=10, width=10, bg="#D0CD94", fg="#241623", highlightbackground="#D0CD94")
    la = Label(fen, text="Flèches directionnelles pour bouger", bg="#D56F3E", fg="#241623")
    la2 = Label (fen, text="\"a\" pour tirer, \"espace\" pour sauter", bg="#C7EF00", fg="#241623")
    entree.grid(padx=15, pady=10, row=0, column=0)
    bout.grid(padx=15, pady=10, row=0, column=1)
    la.grid(padx=5, row=1, columnspan=2)
    la2.grid(padx=5, row = 2, columnspan=2)
    boutc.grid(padx=5, pady=5, row=3, columnspan=2)
    la3.destroy()
    if en <= 3 and p == -1 :
        la3 = Label(fen, text="Vous êtes nul !", bg="#D56F3E", fg="#241623")
        la3.grid(padx=5, row=4, columnspan=2)
    if en >= 8 and p == 1 :
        la3 = Label(fen, text="Vous êtes fort !", bg="#C7EF00", fg="#241623")
        la3.grid(padx=5, row=4, columnspan=2)
    en = en + p
    if en == 11 :
        en = 10
    if en == 0 :
        en = 1
    entree.delete(0,en)
    entree.insert(0,en)
    
def credi(): # générer le niveau spécial "crédits"
    global fen, can, bout, boutc, entree, la, la2, la3, xa, ya, yd, xd, x1, y1, ob, vi, oval, p, co
    ob = []
    p = 0
    unbind()
    bout.destroy()
    boutc.destroy()
    entree.destroy()
    la.destroy()
    la2.destroy()
    la3.destroy()
    fen.title("Squared Blockers Credits")
    can = Canvas(fen,bg="#D0CD94",height=600,width=900)
    can.pack()
    can.update_idletasks()
    time.sleep(1)

    x1, y1 = 855, 135
    xd, yd = 15, 105
    xa, ya = 885, 585

    de = can.create_rectangle(xd, yd, xd, yd, fill="#D56F3E", outline="#D0CD94")
    ar = can.create_rectangle(xa, ya, xa, ya, fill="#C7EF00", outline="#D0CD94")
    
    carre(105, 75, 10)
    carre( 75, 75, 10)
    carre( 45, 75, 10)
    carre( 45,105, 10)
    carre( 45,135, 10)
    carre( 75,135, 10)
    carre(105,135, 10)
    carre(105,165, 10)
    carre(105,195, 10)
    carre( 75,195, 10)
    carre( 45,195, 10)
    
    carre(195,165, 10)
    carre(165,165, 10)
    carre(165,135, 10)
    carre(165,105, 10)
    carre(165, 75, 10)
    carre(195, 75, 10)
    carre(225, 75, 10)
    carre(225,105, 10)
    carre(225,135, 10)
    carre(225,165, 10)
    carre(225,195, 10)
    
    carre(285, 75, 10)
    carre(285,105, 10)
    carre(285,135, 10)
    carre(285,165, 10)
    carre(285,195, 10)
    carre(315,195, 10)
    carre(345,195, 10)
    carre(345,165, 10)
    carre(345,135, 10)
    carre(345,105, 10)
    carre(345, 75, 10)

    carre(405,195, 10)
    carre(405,165, 10)
    carre(405,135, 10)
    carre(405,105, 10)
    carre(405, 75, 10)
    carre(435, 75, 10)
    carre(465, 75, 10)
    carre(465,105, 10)
    carre(465,135, 10)
    carre(435,135, 10)
    carre(465,165, 10)
    carre(465,195, 10)

    carre(525,195, 10)
    carre(525,165, 10)
    carre(525,135, 10)
    carre(525,105, 10)
    carre(525, 75, 10)
    carre(555, 75, 10)
    carre(585, 75, 10)
    carre(585,105, 10)
    carre(585,135, 10)
    carre(555,135, 10)
    carre(555,165, 10)
    carre(585,195, 10)

    carre(705, 75, 10)
    carre(675, 75, 10)
    carre(645, 75, 10)
    carre(645,105, 10)
    carre(645,135, 10)
    carre(645,165, 10)
    carre(645,195, 10)
    carre(675,195, 10)
    carre(705,195, 10)
    carre(675,135, 10)
    carre(705,135, 10)
    
    carre(765,195, 10)
    carre(765,165, 10)
    carre(765,135, 10)
    carre(765,105, 10)
    carre(765, 75, 10)
    carre(795, 75, 10)
    carre(825,105, 10)
    carre(825,135, 10)
    carre(825,165, 10)
    carre(795,195, 10)

    carre( 45,375, 10)
    carre( 45,345, 10)
    carre( 45,315, 10)
    carre( 45,285, 10)
    carre( 45,255, 10)
    carre( 75,255, 10)
    carre(105,285, 10)
    carre( 75,315, 10)
    carre(105,345, 10)
    carre( 75,375, 10)
    
    carre(165,255, 10)
    carre(165,285, 10)
    carre(165,315, 10)
    carre(165,345, 10)
    carre(165,375, 10)
    carre(195,375, 10)

    carre(255,255, 10)
    carre(255,285, 10)
    carre(255,315, 10)
    carre(255,345, 10)
    carre(255,375, 10)
    carre(285,375, 10)
    carre(315,375, 10)
    carre(315,345, 10)
    carre(315,315, 10)
    carre(315,285, 10)
    carre(315,255, 10)
    carre(285,255, 10)

    carre(405,255, 10)
    carre(375,255, 10)
    carre(375,285, 10)
    carre(375,315, 10)
    carre(375,345, 10)
    carre(375,375, 10)
    carre(405,375, 10)
    
    carre(465,255, 10)
    carre(465,285, 10)
    carre(465,315, 10)
    carre(465,345, 10)
    carre(465,375, 10)
    carre(495,315, 10)
    carre(525,285, 10)
    carre(525,255, 10)
    carre(525,345, 10)
    carre(525,375, 10)
    
    carre(615,255, 10)
    carre(585,255, 10)
    carre(585,285, 10)
    carre(585,315, 10)
    carre(585,345, 10)
    carre(585,375, 10)
    carre(615,375, 10)
    carre(615,315, 10)
    
    carre(675,375, 10)
    carre(675,345, 10)
    carre(675,315, 10)
    carre(675,285, 10)
    carre(675,255, 10)
    carre(705,255, 10)
    carre(735,255, 10)
    carre(735,285, 10)
    carre(735,315, 10)
    carre(705,315, 10)
    carre(705,345, 10)
    carre(735,375, 10)

    carre(855,225, 10)
    carre(855,255, 10)
    carre(825,255, 10)
    carre(795,255, 10)
    carre(795,285, 10)
    carre(795,315, 10)
    carre(825,315, 10)
    carre(855,315, 10)
    carre(855,345, 10)
    carre(855,375, 10)
    carre(825,375, 10)
    carre(795,375, 10)
    
    carre( 45,555, 10)
    carre( 45,525, 10)
    carre( 45,495, 10)
    carre( 45,465, 10)
    carre( 45,435, 10)
    carre( 75,435, 10)
    carre(105,465, 10)
    carre( 75,495, 10)
    carre(105,525, 10)
    carre( 75,555, 10)
    
    carre(165,435, 10)
    carre(165,465, 10)
    carre(195,465, 10)
    carre(225,465, 10)
    carre(225,435, 10)
    carre(195,495, 10)
    carre(195,525, 10)
    carre(195,555, 10)
    
    carre(255,555, 10)
    
    carre(315,435, 10)
    carre(315,465, 10)
    carre(315,495, 10)
    carre(315,525, 10)
    carre(315,555, 10)
    carre(345,555, 10)
    carre(375,555, 10)
    
    carre(435,555, 10)
    carre(435,525, 10)
    carre(435,495, 10)
    carre(435,465, 10)
    carre(435,435, 10)
    carre(465,435, 10)
    carre(495,435, 10)
    carre(495,465, 10)
    carre(495,495, 10)
    carre(465,495, 10)
    carre(465,525, 10)
    carre(495,555, 10)
    
    carre(555,435, 10)
    carre(585,435, 10)
    carre(615,435, 10)
    carre(585,465, 10)
    carre(585,495, 10)
    carre(585,525, 10)
    carre(585,555, 10)
    carre(555,555, 10)
    
    carre(675,555, 10)
    carre(675,525, 10)
    carre(675,495, 10)
    carre(675,465, 10)
    carre(675,435, 10)
    carre(705,435, 10)
    carre(735,435, 10)
    carre(735,465, 10)
    carre(735,495, 10)
    carre(705,495, 10)
    carre(705,525, 10)
    carre(735,555, 10)
    
    carre(855,435, 10)
    carre(825,435, 10)
    carre(795,435, 10)
    carre(795,465, 10)
    carre(795,495, 10)
    carre(795,525, 10)
    carre(795,555, 10)
    carre(825,555, 10)
    carre(885,555, 10)
    carre(885,525, 10)
    carre(885,495, 10)
    carre(855,495, 10)

    while len(ob) <= 650 :
        ob.append(str(0))
    
    oval = can.create_oval(x1, y1, x1, y1, fill="#3C787E", outline="#3C787E")
    
    i = 0
    while i <= taille :
        can.coords(oval, x1-i, y1-i, x1+i, y1+i)
        i = i + 1
        can.update_idletasks()
        time.sleep(vi*500)

    i = 0
    while i <= 15:
        can.coords(de, xd-i, yd-i, xd+i, yd+i)
        i = i + 1
        can.update_idletasks()
        time.sleep(vi*100)

    i = 0
    while i <= 15:
        can.coords(ar, xa-i, ya-i, xa+i, ya+i)
        i = i + 1
        can.update_idletasks()
        time.sleep(vi*100)

    co = "b"
    tir("event")
    can.create_rectangle(840, 209, 870, 239, fill="#D0CD94", outline="#D0CD94")
    
    co = "g"
    for i in range (0, 14):
        saut("event")

    ob.append(str(xd)+str(yd))
    ob.append(str(xa)+str(ya))
    
    fen.after_idle(bind)


### programme de base ###

# générer le menu de sélection pour la première fois

fen = Tk()
fen.title("Squared Blockers")
fen["bg"]="#D0CD94"
bout = Button(fen, command=canv, text="--> Jouer <--", bg="#D0CD94", fg="#241623", cursor="hand1", highlightbackground="#D0CD94", activebackground="#3C787E")
boutc = Button(fen, command=credi, text="Crédits (niveau spécial!)", bg="#D0CD94", fg="#241623", cursor="hand1", highlightbackground="#D0CD94", activebackground="#241623", activeforeground="#D0CD94")
entree = Spinbox(fen, from_=1, to=10, width=10, bg="#D0CD94", fg="#241623", highlightbackground="#D0CD94")
entree.delete(0,5)
entree.insert(0,5)
en = entree.get()
la = Label(fen, text="Flèches directionnelles pour bouger", bg="#D56F3E", fg="#241623")
la2 = Label (fen, text="\"a\" pour tirer, \"espace\" pour sauter", bg="#C7EF00", fg="#241623")
la3 = Label(fen, text="", bg="#D56F3E", fg="#241623")
entree.grid(padx=5, pady=5, row=0, column=0)
bout.grid(padx=5, pady=10, row=0, column=1)
la.grid(padx=5, row=1, columnspan=2)
la2.grid(padx=5, row = 2, columnspan=2)
boutc.grid(padx=5, pady=5, row=3, columnspan=2)

### mise en boucle ### 

fen.mainloop()

### fin ###
