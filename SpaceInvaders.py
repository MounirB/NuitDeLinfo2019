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
from tkinter import messagebox
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
        canvas.delete(ALL)
        root.after(1500, Titre)


# On afficher le nom du jeu à l'écran
def Titre():
    global game
    if not game.start:
        canvas.create_text(320, 240, font=('Fixedsys', 24), text="SPACE INVADERS", fill='blue')
        root.after(2000, Titre2)


# On affiche le nom de l'auteur ( It's me !! :p )
def Titre2():
    global game
    if not game.start:
        canvas.create_text(320, 270, font=('Freshbot', 18), text="By Shakan972", fill='red')
        root.after(3000, LoadMeilleurScore)


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
        root.after(2000, MessageRecord)
    else:
        root.after(15000, EcranDePresentation)
    FichierScore.close()


# Cette fonction affiche un message
# lui indiquant qu'il a établit un
# nouveau record :D
def MessageRecord():
    canvas.delete(ALL)
    canvas.create_text(320, 240, font=('Georgia', 18), text="Vous avez établi un nouveau record !!", fill='red')
    root.after(3000, LoadMeilleurScore)


# Quant à cette fonction elle va permettre
# de lire le meilleur score afin de l'afficher
def LoadMeilleurScore():
    global game
    if game.start:
        # FichierScore=open('HighScore','r')
        # lecture=pickle.load(FichierScore)
        lecture = "WIN"
        canvas.delete(ALL)
        canvas.create_text(320, 240, font=('Fixedsys', 24), text="HIGH SCORE", fill='blue')
        canvas.create_text(320, 270, font=('Fixedsys', 24), text=str(lecture), fill='blue')
        FichierScore.close()
        root.after(3000, EcranDePresentation)


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


# Cette fonction permet d'effacer
# le nombre de point gagnés et affichés
# suite à la destruction d'un ennemi
def EffacerScore():
    global afficherScore
    canvas.delete(afficherScore[0])
    afficherScore = afficherScore[1:]


# Cette fonction permet d'afficher
# le nombre de points gagnés à la suite
# de la destruction d'un ennemi
def bla(donnee, x, y, x2, y2):
    global afficherScore
    afficherScore.append(canvas.create_text(x + x2, y + y2,
                                            font=('Fixedsys', 8),
                                            text=str(donnee)+' pts', fill='red'))
    root.after(1500, EffacerScore)


# La fonction ci-dessous permet
# d'animer le canon mobile selon
# la direction choisie par le joueur
def move(dx):
    global game
    if game.student.lives != 0 and not game.paused:
        game.student.x += dx
        if game.student.x <= X_LIMIT[0]:
            game.student.x = X_LIMIT[0]
        elif game.student.x >= X_LIMIT[1]:
            game.student.x = X_LIMIT[1]
        game.student.redraw()



# Cette fonction gère le tir des ennemis
# et vérifie si un a atteint le canon
# mobile du joueur
def launch_enemy_missile():
    global game
    if not game.paused and game.start and game.enemies:
        root.after(1000, launch_enemy_missile)
        # Choose enemy that fires missil
        enemy = game.enemies[random.randint(0, len(game.enemies)-1)]
        game.enemies_missile.append(EnemyMissile(enemy.x, enemy.y))
        

# Cette fonction permet d'animer l'obus tiré
# par un ennemi
def animate_enemies_missile():
    global game
    if game.enemies_missile:
        for missile in game.enemies_missile:
            missile.move()

            # Si un tir ennemi parvient à son objectif en
            # touchant le canon mobile du joueur ben il crève ==> partie terminée !! :p
            if missile.x >= game.student.x and missile.x <= game.student.x+60 and \
                    missile.y >= game.student.y:
                game.student.explod()
                missile.explod()

                game.stop_animation()
                
                if game.student.lives >= 1:
                    AffichageVie.configure(text="Vies : "+str(game.student.lives), font=('Fixedsys',16))
                    root.after(500, game.student.revive())
                else:

                    # On efface l'écran
                    canvas.delete(ALL)
                    AffichageVie.configure(text="Vies : " + str(game.student.lives),font=('Fixedsys',16))
                    image()
                    canvas.create_text(320, 240, font=('Fixedsys', 18), text="Game Over !!", fill='red')
                    game.stop_animation()
                    game.start = False

                    # On vérifie le score
                    SaveMeilleurScore(game.score)


# Cette fonction va permettre d'afficher un
# paysage post-apocalyptique si le joueur
# fait un game over !! :( :(
def image():
    global photo
    photo=PhotoImage(file='apocalypse.GIF')
    canvas.create_image(320, 240, image=photo)

    
# Cette fonction va permettre de gérer le tir du canon
# ainsi que les collisions avec les cibles situées en
# haut du canevas :)
def launch_missile(event):
    global game
    if game.start:
        if not game.paused:
            game.missiles.append(Missile(game.student.x, game.student.y - 20))
            if game.missiles:
                time.sleep(0.09)


# Cette fonction va permettre d'animer l'obus tiré par
# le canon mobile
def animate_missile():
    global game
    if game.missiles:
        for missile in game.missiles:
            missile.move()

            for enemy in game.enemies:
                if missile.x+5 >= enemy.x and missile.x-5 <= enemy.x+60 and\
                        missile.y+5 >= enemy.y and missile.y-5 <= enemy.y+60:
                    game.score += 50
                    missile.explod()
                    AffichageScore.configure(text="Score : "+str(game.score), font=('Fixedsys',16))
                    bla(50, enemy.x, enemy.y, 30, 20)
                    enemy.explod()
                    game.enemies.remove(enemy)

            # if no more enemies
            if not game.enemies:
                game.stop_animation()
                root.after(500, game.init_board)
    

# Les deux fonctions ci-dessous permettent
# de diriger le canon mobile de gauche à droite
def right(event):
    global game
    if game.start and not game.paused:
        move(20)


def left(event):
    global game
    if game.start and not game.paused:
        move(-20)


def main_animation(itr):
    global game
    if game.start and not game.stop_animations and game.itr == itr:
        animate_enemies_missile()
        animate_missile()
        root.after(50, main_animation, itr)


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
    A peaceful Student
    """
    def __init__(self):
        self.x = X_LIMIT[0] + X_LIMIT[1]//2
        self.y = Y_LIMIT[1] - 15
        self.body = canvas.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill='green')
        self.lives = 3

    def explod(self):
        canvas.delete(self.body)

    def revive(self):
        global game
        self.x = X_LIMIT[0] + X_LIMIT[1]//2
        self.y = Y_LIMIT[1] - 5
        canvas.delete(self.body)
        self.body = canvas.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill='green')
        self.lives -= 1
        game.launch_animation()

    def redraw(self):
        canvas.delete(self.body)
        self.body = canvas.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill='green')


class Enemy:
    """
    Too many things, life can be rough
    """
    def __init__(self):
        self.x = random.randint(X_LIMIT[0], X_LIMIT[1])
        self.y = random.randint(Y_LIMIT[0], Y_LIMIT[1]//4)
        self.body = None
        self.type = "default"
        self.text = ["", "", ""]
        self.img = None
        self.set_body()

    def set_body(self):
        self.body = canvas.create_rectangle( self.x + 60, self.y + 20, fill='blue')

    def explod(self):
        global game
        canvas.delete(self.body)
        game.paused = True
        game.stop_animation()
        Message(self.message(phase=game.phase))
        game.paused = False
        game.launch_animation()

    def redraw(self):
        canvas.delete(self.body)
        self.body = []
        self.set_body()

    def message(self, phase):
        return self.text[phase]


class Loyer(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Loyer'
        self.text = ["Etes-vous dépassé par votre loyer ? ",
                     "Pensez à faire une simulation d'une aide au logement auprès de la CAF. "
                     "Visitez le site de la caf sur : http://www.caf.fr/"]
        self.img = PhotoImage(file='img/loyer_180x40.gif')
        self.set_body()

    def set_body(self):
        if self.img is not None:
            self.body = canvas.create_image(self.x, self.y, image=self.img)


class Alcool(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Alcool'
        self.text = ["Passer des soirées top arrosées est dangereux pour votre assiduité.",
                     "Si l'alcool vous mène la vie dure, "
                     "bénéficiez d'une aide anonyme en appelant le 0 980 980 930."]


class Drogue(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Drogue'
        self.text = ["La consommation de drogue est dangereuse pour votre santé ...et votre diplôme. ",
                     "Si vous n'arrivez pas à vous débarrasser de votre addiction. "
                     "Faites-vous aider en appelant anonymement le 0 800 23 13 13"]


class Paperasse(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Paperasse'
        self.text = ["Les démarches administratives sont entrain de vous faire perdre la tête. ",
                     "Visitez le nouveau site mis à disposition des étudiants qui regroupe toutes les démarches."
                     "https://www.etudiant.gouv.fr/"]


class MST(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'MST'
        self.text = ["N'oubliez jamais de sortir protégé !",
                     "En cas de doutes, faites-vous dépister !"
                     "Renseignez-vous sur https://www.sida-info-service.org/ "]


class Missile:
    """
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, fill='yellow')
        self.dy = MISSILE_DY

    def explod(self):
        global game
        canvas.delete(self.body)
        game.missiles.remove(self)

    def move(self):
        self.y -= self.dy
        if self.y <= Y_LIMIT[0]:
            self.explod()
        else:
            self.redraw()

    def redraw(self):
        canvas.delete(self.body)
        self.body = canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, fill='yellow')


class EnemyMissile:
    """
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = canvas.create_oval(self.x, self.y, self.x + 4, self.y + 20, fill='orange')
        self.dy = ENEMIES_MISSILE_DY

    def explod(self):
        global game
        canvas.delete(self.body)
        game.enemies_missile.remove(self)

    def move(self):
        self.y += self.dy
        if self.y >= Y_LIMIT[1]:
            self.explod()
        else:
            self.redraw()

    def redraw(self):
        canvas.delete(self.body)
        self.body = canvas.create_oval(self.x, self.y, self.x + 4, self.y + 20, fill='orange')


class Game:
    """

    """
    def __init__(self):
        self.start = False
        self.stop_animations = False
        self.score = 0
        self.phase = 0
        self.student = Student()
        self.missiles = []
        self.enemies = []
        self.enemies_missile = []
        self.paused = False
        self.paused_body = None
        self.itr = 0

    def init_board(self):
        canvas.delete(ALL)
        self.score = 0
        self.student = Student()
        self.missiles = []
        self.enemies = []
        self.enemies_missile = []
        for _ in range(NB_START_ENEMIES):
            self.enemies.append(Loyer())

        # On efface tout à l'écran
        background = PhotoImage(file='earth.gif')
        canvas.create_image(240, 320, image=background)

        AffichageScore.configure(text="Score : " + str(self.score))
        AffichageVie.configure(text="Vies : " + str(self.student.lives))

        self.start = True
        self.paused = False
        self.stop_animations = False
        self.launch_main_animation()
        root.after(1000, launch_enemy_missile())

    def launch_main_animation(self):
        self.itr += 1
        main_animation(self.itr)

    def stop_animation(self):
        self.stop_animations = True

    def launch_animation(self):
        self.stop_animations = False
        self.launch_main_animation()

    def pause_pressed(self):
        if self.paused:
            self.paused = False
            canvas.delete(self.paused_body)
            self.launch_animation()
        else:
            self.paused = True
            self.paused_body = canvas.create_text(320, 240, font=('Fixedsys', 18), text="PAUSE")
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
    ENEMIES_MISSILE_DY = 3
    MISSILE_DY = 10

    # Création de la fenêtre principale

    root = Tk()

    # Titre de la fenêtre

    root.title('University Invaders')

    # Définition du canevas ( Ecran de jeu )

    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')

    # Définition des touches qui vont permettre
    # de diriger le canon mobile

    canvas.bind_all("<Right>", right)
    canvas.bind_all("<Left>", left)
    canvas.bind_all("<space>", launch_missile)
    canvas.bind_all("<p>", pause)

    canvas.grid(row=1, column=0, columnspan=2, rowspan=3)

    # Installation d'une image de fond
    # pour être plus dans l'ambiance 8)


    # Définition des boutons

    # Ce bouton permet de commencer une nouvelle partie

    Button(root, text="Nouvelle partie", command=new_game).grid(row=2, column=2, sticky=N, padx=5)
    Button(root, text="Quitter", command=root.destroy).grid(row=3, column=2, sticky=N, padx=5)


    # On affiche les indications concernant
    # le score et les vies restantes du joueur

    AffichageScore=Label(root, font=('Fixedsys', 16))
    AffichageVie=Label(root, font=('Fixedsys', 16))
    AffichageScore.grid(row=0,column=0,sticky=W)
    AffichageVie.grid(row=0,column=1,sticky=E)

    afficherScore = []

    # Cette variable va permettre de suspendre certaines
    # fonctions durant l'affichage de l'écran de présentation

    # Si le fichier contenant les scores n'existe pas
    # on le crée avec comme valeur de départ ==> 0

    if existe('HighScore')==0:
        FichierScore=open('HighScore', 'w')
        pickle.dump(0,FichierScore)
        FichierScore.close()

    game = Game()

    # On affiche l'écran de présentation du jeu

    EcranDePresentation()

    # On met le gestionnaire d'événements en route

    root.mainloop()

