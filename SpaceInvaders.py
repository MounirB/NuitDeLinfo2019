#####################################
#                                   #
#  Programme : University invaders  #
#  Auteur : Les 3 Mousquethesards   #
#  Date de creation : 06/12/19      #
#                                   #
#####################################


from tkinter import *
from tkinter import messagebox
import random
import time
import pickle


def EcranDePresentation():
    global game
    if not game.start:
        AffichageScore.configure(text="",font=('Fixedsys',16))
        AffichageVie.configure(text="",font=('Fixedsys',16))
        canvas.delete(ALL)
        root.after(1500, Titre)


def Titre():
    global game
    if not game.start:
        canvas.create_text(260, 240, font=('Fixedsys', 24), text="UNIVERSITY INVADERS", fill='blue')
        root.after(2000, Titre2)


# On affiche le nom des auteurs
def Titre2():
    global game
    if not game.start:
        canvas.create_text(280, 270, font=('Freshbot', 18), text="By Les 3 Mousquethesards", fill='red')
        root.after(3000, LoadMeilleurScore)


# Cette fonction va permettre d'enregistrer
# le meilleur score
def SaveMeilleurScore(resultat):
    return None


def MessageRecord():
    canvas.delete(ALL)
    canvas.create_text(320, 240, font=('Georgia', 18), text="Vous avez etabli un nouveau record !!", fill='red')
    root.after(3000, LoadMeilleurScore)

def LoadMeilleurScore():
    global game
    if game.start:
        # FichierScore=open('HighScore','r')
        # lecture=pickle.load(FichierScore)
        lecture = "WIN"
        canvas.delete(ALL)
        canvas.create_text(320, 240, font=('Fixedsys', 24), text="HIGH SCORE", fill='blue')
        canvas.create_text(320, 270, font=('Fixedsys', 24), text=str(lecture), fill='blue')
        # FichierScore.close()
        root.after(3000, EcranDePresentation)


def existe(fname):
    try:
        f=open(fname,'r')
        f.close()
        return 1
    except:
        return 0


def new_game():
    global game
    game.init_board()


def EffacerScore():
    global afficherScore
    canvas.delete(afficherScore[0])
    afficherScore = afficherScore[1:]


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
    if game.student.lives >= 0 and not game.paused:
        game.student.x += dx
        if game.student.x <= X_LIMIT[0]:
            game.student.x = X_LIMIT[0]
        elif game.student.x >= X_LIMIT[1]:
            game.student.x = X_LIMIT[1]
        game.student.redraw()



def launch_enemy_missile(itr):
    global game
    if not game.paused and game.start and game.enemies and game.itr == itr:
        root.after(1000, launch_enemy_missile, itr)
        # Choose enemy that fires missil
        enemy = game.enemies[random.randint(0, len(game.enemies)-1)]
        game.enemies_missile.append(EnemyMissile(enemy.x, enemy.y))


def animate_enemies_missile():
    global game
    if game.enemies_missile:
        for missile in game.enemies_missile:
            missile.move()
            if missile.x >= game.student.x and missile.x <= game.student.x+60 and \
                    missile.y >= game.student.y:
                game.student.explod()
                missile.explod()

                game.stop_animation()
                
                if game.student.lives >= 1:
                    root.after(500, game.student.revive())
                else:
                    canvas.delete(ALL)
                    AffichageVie.configure(text="Vies : " + str(0), font=('Fixedsys',16))
                    image()
                    canvas.create_text(320, 240, font=('Fixedsys', 18), text="Game Over !!", fill='red')
                    game.stop_animation()
                    game.start = False
                    SaveMeilleurScore(game.score)


def image():
    global photo
    photo=PhotoImage(file='img/apocalypse.GIF')
    canvas.create_image(320, 240, image=photo)


def launch_missile(event):
    global game
    if game.start:
        if not game.paused:
            game.missiles.append(Missile(game.student.x, game.student.y - 20))
            if game.missiles:
                time.sleep(0.09)


def animate_missile():
    global game
    if game.missiles:
        for missile in game.missiles:
            missile.move()

            for enemy in game.enemies:
                if missile.x+5 >= enemy.x and missile.x-5 <= enemy.x+180 and\
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

    if game.start and not game.student.lives == 0:
        game.pause_pressed()


class Student:
    """
    A peaceful Student
    """
    def __init__(self):
        self.x = X_LIMIT[0] + X_LIMIT[1]//2
        self.y = Y_LIMIT[1] - 40
        self.img = PhotoImage(file='img/student_40x100.gif')
        self.body = canvas.create_image(self.x, self.y, image=self.img)
        self.lives = 3

    def explod(self):
        canvas.delete(self.body)

    def revive(self):
        global game
        self.x = X_LIMIT[0] + X_LIMIT[1]//2
        self.y = Y_LIMIT[1] - 40
        canvas.delete(self.body)
        self.body = canvas.create_image(self.x, self.y, image=self.img)
        self.lives -= 1
        AffichageVie.configure(text="Vies : " + str(game.student.lives), font=('Fixedsys', 16))
        game.launch_animation()

    def redraw(self):
        canvas.delete(self.body)
        self.body = canvas.create_image(self.x, self.y, image=self.img)


class Enemy:
    """
    Too many things, life can be rough
    """
    def __init__(self):
        self.x = random.randint(X_LIMIT[0]+10, X_LIMIT[1]-10)
        self.y = random.randint(Y_LIMIT[0]+10, Y_LIMIT[1]//4)
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
        messagebox.showinfo("Info", self.message(phase=game.phase))
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
        self.img = PhotoImage(file='img/alcool_180x40.gif')
        self.set_body()

    def set_body(self):
        if self.img is not None:
            self.body = canvas.create_image(self.x, self.y, image=self.img)


class Drogue(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Drogue'
        self.text = ["La consommation de drogue est dangereuse pour votre santé ...et votre diplôme. ",
                     "Si vous n'arrivez pas à vous débarrasser de votre addiction. "
                     "Faites-vous aider en appelant anonymement le 0 800 23 13 13"]
        self.img = PhotoImage(file='img/drogue_180x40.gif')
        self.set_body()

    def set_body(self):
        if self.img is not None:
            self.body = canvas.create_image(self.x, self.y, image=self.img)


class Paperasse(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Paperasse'
        self.text = ["Les démarches administratives sont entrain de vous faire perdre la tête. ",
                     "Visitez le nouveau site mis à disposition des étudiants qui regroupe toutes les démarches."
                     "https://www.etudiant.gouv.fr/"]
        self.img = PhotoImage(file='img/paperasse_180x40.gif')
        self.set_body()

    def set_body(self):
        if self.img is not None:
            self.body = canvas.create_image(self.x, self.y, image=self.img)


class MST(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'MST'
        self.text = ["N'oubliez jamais de sortir protégé !",
                     "En cas de doutes, faites-vous dépister !"
                     "Renseignez-vous sur https://www.sida-info-service.org/ "]
        self.img = PhotoImage(file='img/mst_180x40.gif')
        self.set_body()

    def set_body(self):
        if self.img is not None:
            self.body = canvas.create_image(self.x, self.y, image=self.img)


class Missile:
    """
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = PhotoImage(file='img/book_40x40.gif')
        self.body = canvas.create_image(self.x, self.y, image=self.img)
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
        self.body = canvas.create_image(self.x, self.y, image=self.img)


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
        self.generate_enemies()

        # background = PhotoImage(file='img/vid.gif', format="gif -index 2")
        # canvas.create_image(100, 100, image=background)

        AffichageScore.configure(text="Score : " + str(self.score))
        AffichageVie.configure(text="Vies : " + str(self.student.lives))

        self.start = True
        self.paused = False
        self.stop_animations = False
        self.launch_main_animation()

    def generate_enemies(self):
        self.enemies.append(Loyer())
        self.enemies.append(MST())
        self.enemies.append(Paperasse())
        self.enemies.append(Alcool())
        self.enemies.append(Drogue())

    def launch_main_animation(self):
        self.itr += 1
        root.after(1000, launch_enemy_missile, self.itr)
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
    WIDTH = 480
    HEIGHT = 630
    MARGIN = 5
    X_LIMIT = [MARGIN, WIDTH-MARGIN]
    Y_LIMIT = [MARGIN, HEIGHT-MARGIN]

    NB_START_ENEMIES = 4
    NB_LIVES_START = 3
    ENEMIES_MISSILE_DY = 3
    MISSILE_DY = 10

    root = Tk()

    root.title('University Invaders')

    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')


    canvas.bind_all("<Right>", right)
    canvas.bind_all("<Left>", left)
    canvas.bind_all("<space>", launch_missile)
    canvas.bind_all("<p>", pause)

    canvas.grid(row=1, column=0, columnspan=2, rowspan=3)

    Button(root, text="Nouvelle partie", command=new_game).grid(row=2, column=2, sticky=N, padx=5)
    Button(root, text="Quitter", command=root.destroy).grid(row=3, column=2, sticky=N, padx=5)


    # On affiche les indications concernant
    # le score et les vies restantes du joueur

    AffichageScore=Label(root, font=('Fixedsys', 16))
    AffichageVie=Label(root, font=('Fixedsys', 16))
    AffichageScore.grid(row=0,column=0,sticky=W)
    AffichageVie.grid(row=0,column=1,sticky=E)

    afficherScore = []

    if existe('HighScore')==0:
        FichierScore=open('HighScore', 'w')
        pickle.dump(0,FichierScore)
        FichierScore.close()

    game = Game()

    EcranDePresentation()

    root.mainloop()

