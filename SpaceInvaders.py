# -*- coding: cp1252 -*-

###################################
#                                 #
#  Programme : Space invaders     #
#  Auteur : Shakan972             #
#  Date de creation : 13/04/07    #
#                                 #
###################################


##########################################
#                                        #
# Importations des fonctions nécessaires #
#                                        #
##########################################

from tkinter import *
import random
import time
import pickle

############################
#                          #
# Définition des fonctions #
#                          #
############################


# Cette fonction affiche l'écran de présentation du jeu
def EcranDePresentation():
    global game
    if not game.start:
        AffichageScore.configure(text="",font=('Fixedsys',16))
        AffichageVie.configure(text="",font=('Fixedsys',16))
        can.delete(ALL)
        fen.after(1500,Titre)


# On afficher le nom du jeu à l'écran
def Titre():
    global game
    if game.start != 1:
        can.create_text(320,240,font=('Fixedsys',24),text="SPACE INVADERS",fill='blue')
        fen.after(2000, Titre2)


# On affiche le nom de l'auteur ( It's me !! :p )
def Titre2():
    global game
    if game.start != 1:
        can.create_text(320,270,font=('Freshbot',18),text="By Shakan972",fill='red')
        fen.after(3000,LoadMeilleurScore)


# Cette fonction va permettre d'enregistrer
# le meilleur score
def SaveMeilleurScore(resultat):
    FichierScore=open('HighScore','r')
    lecture=pickle.load(FichierScore)

    # Si le score réalisé à la fin de la partie
    # est supérieur à celui déjà enregistré dans le fichier
    # alors on remplace ce dernier par le nouveau score record
    
    if resultat>lecture:
        FichierScore=open('HighScore','w')
        pickle.dump(resultat,FichierScore)
        FichierScore.close()
        fen.after(2000,MessageRecord)
    else:
        fen.after(15000,EcranDePresentation)
    FichierScore.close()


# Cette fonction affiche un message
# lui indiquant qu'il a établit un
# nouveau record :D
def MessageRecord():
    can.delete(ALL)
    can.create_text(320,240,font=('Georgia',18),text="Vous avez établi un nouveau record !!",fill='red')
    fen.after(3000,LoadMeilleurScore)


# Quant à cette fonction elle va permettre
# de lire le meilleur score afin de l'afficher
def LoadMeilleurScore():
    global game
    if game.start:
        # FichierScore=open('HighScore','r')
        # lecture=pickle.load(FichierScore)
        lecture = "WIN"
        can.delete(ALL)
        can.create_text(320,240,font=('Fixedsys',24),text="HIGH SCORE",fill='blue')
        can.create_text(320,270,font=('Fixedsys',24),text=str(lecture),fill='blue')
        FichierScore.close()
        fen.after(3000,EcranDePresentation)


# Cette fonction permet de vérifier
# l'existence d'un fichier
def existe(fname):
    try:
        f=open(fname,'r')
        f.close()
        return 1
    except:
        return 0


# Cette fonction permet de réinitialiser le jeu
# selon la volonté du joueur de recommencer une partie
def new_game():
    global game
    game.init_board()


# Cette fonction permet d'afficher
# le nombre de points gagnés à la suite
# de la destruction d'un ennemi
def score(donnee, x, y, x2, y2):
    global afficherScore
    afficherScore.append(can.create_text(x+x2, y+y2,
                        font=('Fixedsys', 8),
                        text=str(donnee)+' pts',fill='red'))
    fen.after(1500,EffacerScore)


# Cette fonction permet d'effacer
# le nombre de point gagnés et affichés
# suite à la destruction d'un ennemi
def EffacerScore():
    global afficherScore
    i=0
    while i<len(afficherScore):
        can.delete(afficherScore[i])
        i+=1

# La fonction ci-dessous permet
# d'animer le canon mobile selon
# la direction choisie par le joueur

def move(dx):
    global game

    if game.student.lives != 0 and not game.paused:
   
        game.student.x += dx


        # Si on arrive au bord de l'écran
        # le canon mobile se retrouve bloqué
        # afin de ne pas aller plus loin :p
        
        if game.student.x <= X_LIMIT[0]:
            game.student.x = X_LIMIT[0]
        elif game.student.x >= X_LIMIT[1]:
            game.student.x = X_LIMIT[1]
        game.student.redraw()



# Cette fonction gère le tir des ennemis
# et vérifie si un a atteint le canon
# mobile du joueur
def launch_enemy_missil():
    global game
    if not game.paused:
        if game.start:
            # Choose enemy that fires missil
            enemy = game.enemies[random.randint(0, len(game.enemies))]
            game.enemies_missil.append(EnemyMissil(enemy.x, enemy.y))
            animate_enemies_missil()
    fen.after(100, launch_enemy_missil)
        

# Cette fonction permet d'animer l'obus tiré
# par un ennemi
def animate_enemies_missil():
    global game
    if not game.paused:
        for missil in game.enemies_missil:
            missil.move()

            # Si un tir ennemi parvient à son objectif en
            # touchant le canon mobile du joueur ben il crève ==> partie terminée !! :p
            if missil.x >= game.student.x and missil.x <= game.student.x+60 and \
                    missil.y >= game.student.y:
                game.student.explod()
                missil.explod()

                # Diminution du capital de vies
                # du joueur
                game.stop_animation()
                
                if game.student.lives >=1:
                    AffichageVie.configure(text="Lives : "+str(game.student.lives), font=('Fixedsys',16))
                    fen.after(500, game.student.revive())
                else:

                    # On efface l'écran
                    can.delete(ALL)
                    image()
                    can.create_text(320,240,font=('Fixedsys',18),text="Game Over !!", fill='red')
                    game.stop_animation()
                    game.start = False

                    # On vérifie le score
                    SaveMeilleurScore(game.score)

        fen.after(50, animate_enemies_missil)

# Cette fonction va permettre d'afficher un
# paysage post-apocalyptique si le joueur
# fait un game over !! :( :(

def image():
    global photo
    photo=PhotoImage(file='apocalypse.gif')
    can.create_image(320,240,image=photo)
    

# Cette fonction permet de ressuciter
# le défunt joueur \o/ Amen !! XD
def res_student():
    global game
    if not game.paused:
        game.student.revive()
    

    
# Cette fonction va permettre de gérer le tir du canon
# ainsi que les collisions avec les cibles situées en
# haut du canevas :)
def launch_missil(event):
    global game
    if game.start:
        if not game.paused:
            game.missil = Missil(game.student.x, game.student.y-20)
            if game.missil.fired:
                time.sleep(0.09)
                animate_missil()


# Cette fonction va permettre d'animer l'obus tiré par
# le canon mobile
def animate_missil():
    global game

    if not game.paused and (game.missil is not None) and (not game.stop_animations):
        if game.missil.fired:
            game.missil.move()

            for enemy in game.enemies:
                if game.missil.x+5 >= enemy.x and game.missil.x-5 <= enemy.x+60:
                    if game.missil.y+5 >= enemy.y and game.missil.y-5 <= enemy.y+60:
                        game.score += 50
                        game.missil.explod()
                        AffichageScore.configure(text="Score : "+str(game.score), font=('Fixedsys',16))
                        # score(50, enemy.x, enemy.y, 30, 20)
                        enemy.explod()
                        game.enemies.remove(enemy)

            # if no more enemies
            if not game.enemies:
               game.init_board()
            else:
                fen.after(50, animate_missil)
    

# Les deux fonctions ci-dessous permettent
# de diriger le canon mobile de gauche à droite
def right(event):
    global game
    if game.start:
        if not game.paused:
            move(20)


def left(event):
    global game
    if game.start:
        if not game.paused:
            move(-20)


# Cette fonction permet d'effectuer une pause en cours de partie
def pause(event):
    global game

    # Si le jeu n'a pas commencé
    # la fonction ne démarre pas
    # Il en est de même si le joueur
    # est mort :p
    if game.start and not game.student.lives == 0:
        game.pause_pressed()


class Student:
    """
    A peacfule Student
    """
    def __init__(self):
        self.x = X_LIMIT[0] + X_LIMIT[1]//2
        self.y = Y_LIMIT[1] - 5
        self.body = can.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill='green')
        self.lives = 3

    def explod(self):
        can.delete(self.body)

    def revive(self):
        self.x = X_LIMIT[0] + X_LIMIT[1]//2
        self.y = Y_LIMIT[1] - 5
        can.delete(self.body)
        self.body = can.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill='green')
        self.lives -= 1

    def redraw(self):
        can.delete(self.body)
        self.body = can.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill='green')


class Enemy:
    """
    Too many things, life can be rough
    """
    def __init__(self):
        self.x = random.randint(X_LIMIT[0], X_LIMIT[1])
        self.y = random.randint(Y_LIMIT[0], Y_LIMIT[1]//4)
        self.body = []
        self.body.append(can.create_rectangle(self.x, self.y, self.x + 60, self.y + 20, fill='blue'))
        self.body.append(can.create_rectangle(self.x, self.y, self.x + 20, self.y + 40, fill='blue'))
        self.body.append(can.create_rectangle(self.x + 40, self.y, self.x + 60, self.y + 40, fill='blue'))

    def explod(self):
        for b in self.body:
            can.delete(b)

    def redraw(self):
        for b in self.body:
            can.delete(b)
        self.body = []
        self.body.append(can.create_rectangle(self.x, self.y, self.x + 60, self.y + 20, fill='blue'))
        self.body.append(can.create_rectangle(self.x, self.y, self.x + 20, self.y + 40, fill='blue'))
        self.body.append(can.create_rectangle(self.x + 40, self.y, self.x + 60, self.y + 40, fill='blue'))


class Missil:
    """
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = can.create_oval(self.x, self.y, self.x+20, self.y+20,fill='yellow')
        self.fired = True
        self.dy = 10

    def explod(self):
        self.fired = 0
        can.delete(self.body)

    def move(self):
        self.y -= self.dy
        if self.y <= Y_LIMIT[0]:
            self.explod()
        else:
            self.redraw()

    def redraw(self):
        can.delete(self.body)
        self.body = can.create_oval(self.x, self.y, self.x+20, self.y+20,fill='yellow')


class EnemyMissil:
    """
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = can.create_oval(self.x, self.y, self.x+4, self.y+20,fill='orange')
        self.fired = True
        self.dy = 5

    def explod(self):
        self.fired = 0
        can.delete(self.body)

    def move(self):
        self.y += self.dy
        if self.y >= Y_LIMIT[1]:
            self.explod()
        else:
            self.redraw()

    def redraw(self):
        can.delete(self.body)
        self.body = can.create_oval(self.x, self.y, self.x+4, self.y+20,fill='orange')


class Game:
    """

    """
    def __init__(self):
        self.start = False
        self.stop_animations = False
        self.score = 0
        self.student = Student()
        self.missil = None
        self.enemies = []
        self.enemies_missil = []
        self.paused = False
        self.paused_body = None

    def init_board(self):
        can.delete(ALL)
        self.score = 0
        self.student = Student()
        self.enemies = []
        for _ in range(NB_START_ENEMIES):
            self.enemies.append(Enemy())

        # On efface tout à l'écran
        background = PhotoImage(file='earth.gif')
        can.create_image(240, 320, image=background)

        AffichageScore.configure(text="Score : " + str(self.score))
        AffichageVie.configure(text="Vies : " + str(self.student.lives))

        self.start = True
        self.paused = False
        fen.after(200, launch_enemy_missil())

    def stop_animation(self):
        self.stop_animation = True

    def launch_animation(self):
        self.stop_animations = False
        animate_missil()
        animate_enemies_missil()

    def pause_pressed(self):
        if self.paused:
            self.paused = False
            can.delete(self.paused_body)
            self.launch_animation()
        else:
            self.paused = True
            self.paused_body = can.create_text(320, 240, font=('Fixedsys', 18), text="PAUSE")
            self.stop_animation()



#######################
#                     #
# Programme principal #
#                     #
#######################
if __name__ == "__main__":

    NB_START_ENEMIES = 4
    NB_LIVES_START = 3
    WIDTH = 480
    HEIGHT = 630
    MARGIN = 5
    X_LIMIT = [MARGIN, WIDTH-MARGIN]
    Y_LIMIT = [MARGIN, HEIGHT-MARGIN]

    # Création de la fenêtre principale

    fen=Tk()

    # Titre de la fenêtre

    fen.title('University Invaders')

    # Définition du canevas ( Ecran de jeu )

    can = Canvas(fen, width=WIDTH, height=HEIGHT, bg='black')

    # Définition des touches qui vont permettre
    # de diriger le canon mobile

    can.bind_all("<Right>", right)
    can.bind_all("<Left>", left)
    can.bind_all("<space>", launch_missil)
    can.bind_all("<p>", pause)

    can.grid(row=1, column=0, columnspan=2, rowspan=3)

    # Installation d'une image de fond
    # pour être plus dans l'ambiance 8)


    # Définition des boutons

    # Ce bouton permet de commencer une nouvelle partie

    Button(fen, text="Nouvelle partie", command=new_game).grid(row=2, column=2, sticky=N, padx=5)
    Button(fen, text="Quitter", command=fen.destroy).grid(row=3, column=2, sticky=N, padx=5)


    # On affiche les indications concernant
    # le score et les vies restantes du joueur

    AffichageScore=Label(fen,font=('Fixedsys',16))
    AffichageVie=Label(fen,font=('Fixedsys',16))
    AffichageScore.grid(row=0,column=0,sticky=W)
    AffichageVie.grid(row=0,column=1,sticky=E)

    # Cette variable va permettre de suspendre certaines
    # fonctions durant l'affichage de l'écran de présentation

    # Si le fichier contenant les scores n'existe pas
    # on le crée avec comme valeur de départ ==> 0

    if existe('HighScore')==0:
        FichierScore=open('HighScore','w')
        pickle.dump(0,FichierScore)
        FichierScore.close()

    game = Game()

    # On affiche l'écran de présentation du jeu

    EcranDePresentation()

    # On met le gestionnaire d'événements en route

    fen.mainloop()

