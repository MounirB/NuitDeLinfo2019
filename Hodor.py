from tkinter import *
from tkinter import messagebox
import random
import time
import pickle


def Hold_The_Door():
    global Hold_The_Dooor
    if not Hold_The_Dooor.hold_THEEE_DOOOoooR:
        Hold_The_Doooor.configure(text="",font=('Fixedsys',16))
        Hold_Theee_Door.configure(text="",font=('Fixedsys',16))
        Hooold_The_Door.delete(ALL)
        Hodor.after(1500, Hoooold_The_Dooor)


def Hoooold_The_Dooor():
    global Hold_The_Dooor
    if not Hold_The_Dooor.hold_THEEE_DOOOoooR:
        Hooold_The_Door.create_text(260, 240, font=('Fixedsys', 24), text="UNIVERSITY INVADERS", fill='blue')
        Hodor.after(2000, Hoooold_The_Dooor2)


def Hoooold_The_Dooor2():
    global Hold_The_Dooor
    if not Hold_The_Dooor.hold_THEEE_DOOOoooR:
        Hooold_The_Door.create_text(280, 270, font=('Freshbot', 18), text="By Les 3 Mousquethesards", fill='red')
        Hodor.after(3000, Hoooooooooold_The_Door)


def Hooooooold_The_Door(H):
    return None


def Hol():
    Hooold_The_Door.delete(ALL)
    Hooold_The_Door.create_text(320, 240, font=('Georgia', 18), text="Vous avez etabli un nouveau record !!", fill='red')
    Hodor.after(3000, Hoooooooooold_The_Door)

def Hoooooooooold_The_Door():
    global Hold_The_Dooor
    if Hold_The_Dooor.hold_THEEE_DOOOoooR:
        Hold__The_Door = "WIN"
        Hooold_The_Door.delete(ALL)
        Hooold_The_Door.create_text(320, 240, font=('Fixedsys', 24), text="HIGH SCORE", fill='blue')
        Hooold_The_Door.create_text(320, 270, font=('Fixedsys', 24), text=str(Hold__The_Door), fill='blue')
        Hodor.after(3000, Hold_The_Door)


def existe(Holld_The_Door):
    try:
        HODORRRRrrrrRRRRRRrrrrRRR=open(Holld_The_Door,'r')
        HODORRRRrrrrRRRRRRrrrrRRR.close()
        return 1
    except:
        return 0


def HHold_The_Dooor():
    global Hold_The_Dooor
    Hold_The_Dooor.init_board()


def HOOLD_The_Door():
    global HoOld_The_Door
    Hooold_The_Door.delete(HoOld_The_Door[0])
    HoOld_The_Door = HoOld_The_Door[1:]


def HooLD_The_Door(HoOld_The_Door, hoddor, hodoorr, x2, y2):
    global Hoold_The_DOor
    Hoold_The_DOor.append(Hooold_The_Door.create_text(hoddor + x2, hodoorr + y2,
                                            font=('Fixedsys', 8),
                                            text=str(HoOld_The_Door)+' pts', fill='red'))
    Hodor.after(1500, HOOLD_The_Door)


def Holddedoor(Holdedoor):
    global Hold_The_Dooor
    if Hold_The_Dooor.HOldorR.hhhoooldDEEEEEEEEdoor >= 0 and not Hold_The_Dooor.hOOOOooooOOOld_THEEE_DOOOoooR:
        Hold_The_Dooor.HOldorR.hoddor += Holdedoor
        if Hold_The_Dooor.HOldorR.hoddor <= Holdedooor[0]:
            Hold_The_Dooor.HOldorR.hoddor = Holdedooor[0]
        elif Hold_The_Dooor.HOldorR.hoddor >= Holdedooor[1]:
            Hold_The_Dooor.HOldorR.hoddor = Holdedooor[1]
        Hold_The_Dooor.HOldorR.redraw()



def HOOldedoor(HodoRRRRROOOOORRRRRRRRrrrr):
    global Hold_The_Dooor
    if not Hold_The_Dooor.hOOOOooooOOOld_THEEE_DOOOoooR and Hold_The_Dooor.hold_THEEE_DOOOoooR and Hold_The_Dooor.HoOdDedoor and Hold_The_Dooor.HodoRRRRROOOOORRRRRRRRrrrr == HodoRRRRROOOOORRRRRRRRrrrr:
        Hodor.after(1000, HOOldedoor, HodoRRRRROOOOORRRRRRRRrrrr)
        enemy = Hold_The_Dooor.HoOdDedoor[random.randint(0, len(Hold_The_Dooor.HoOdDedoor)-1)]
        Hold_The_Dooor.HoOdDedoor_holDDoooorr.append(EnemyHolDDoooorr(enemy.hoddor, enemy.hodoorr))


def Hold_dedoor():
    global Hold_The_Dooor
    if Hold_The_Dooor.HoOdDedoor_holDDoooorr:
        for holDDoooorr in Hold_The_Dooor.HoOdDedoor_holDDoooorr:
            holDDoooorr.Holddedoor()
            if holDDoooorr.hoddor >= Hold_The_Dooor.HOldorR.hoddor and holDDoooorr.hoddor <= Hold_The_Dooor.HOldorR.hoddor+60 and \
                    holDDoooorr.hodoorr >= Hold_The_Dooor.HOldorR.hodoorr:
                Hold_The_Dooor.HOldorR.explod()
                holDDoooorr.explod()

                Hold_The_Dooor.stop_animation()
                
                if Hold_The_Dooor.HOldorR.hhhoooldDEEEEEEEEdoor >= 1:
                    Hodor.after(500, Hold_The_Dooor.HOldorR.revive())
                else:
                    Hooold_The_Door.delete(ALL)
                    Hold_Theee_Door.configure(text="Vies : " + str(0), font=('Fixedsys',16))
                    image()
                    Hooold_The_Door.create_text(320, 240, font=('Fixedsys', 18), text="Hold_The_Dooor Over !!", fill='red')
                    Hold_The_Dooor.stop_animation()
                    Hold_The_Dooor.hold_THEEE_DOOOoooR = False
                    Hooooooold_The_Door(Hold_The_Dooor.holdDeDOoOOOOOOrRRRrrr)


def HOLDdeDooRRR():
    global holdeDoor
    holdeDoor=PhotoImage(file='img/apocalypse.GIF')
    Hooold_The_Door.create_image(320, 240, image=holdeDoor)


def HOLDEDOOR(event):
    global Hold_The_Dooor
    if Hold_The_Dooor.hold_THEEE_DOOOoooR:
        if not Hold_The_Dooor.hOOOOooooOOOld_THEEE_DOOOoooR:
            Hold_The_Dooor.holDDoooorrr.append(HolDDoooorr(Hold_The_Dooor.HOldorR.hoddor, Hold_The_Dooor.HOldorR.hodoorr - 20))
            if Hold_The_Dooor.holDDoooorrr:
                time.sleep(0.09)


def ODEODOR():
    global Hold_The_Dooor
    if Hold_The_Dooor.holDDoooorrr:
        for holDDoooorr in Hold_The_Dooor.holDDoooorrr:
            holDDoooorr.Holddedoor()

            for enemy in Hold_The_Dooor.HoOdDedoor:
                if holDDoooorr.hoddor+5 >= enemy.hoddor and holDDoooorr.hoddor-5 <= enemy.hoddor+180 and\
                        holDDoooorr.hodoorr+5 >= enemy.hodoorr and holDDoooorr.hodoorr-5 <= enemy.hodoorr+60:
                    Hold_The_Dooor.holdDeDOoOOOOOOrRRRrrr += 50
                    holDDoooorr.explod()
                    Hold_The_Doooor.configure(text="Vies : "+str(Hold_The_Dooor.holdDeDOoOOOOOOrRRRrrr), font=('Fixedsys',16))
                    HooLD_The_Door(50, enemy.hoddor, enemy.hodoorr, 30, 20)
                    enemy.explod()
                    Hold_The_Dooor.HoOdDedoor.reHolddedoor(enemy)

            if not Hold_The_Dooor.HoOdDedoor:
                Hold_The_Dooor.stop_animation()
                Hodor.after(500, Hold_The_Dooor.init_board)
    

def Holdedddoor(event):
    global Hold_The_Dooor
    if Hold_The_Dooor.hold_THEEE_DOOOoooR and not Hold_The_Dooor.hOOOOooooOOOld_THEEE_DOOOoooR:
        Holddedoor(20)


def Holdedddoorr(event):
    global Hold_The_Dooor
    if Hold_The_Dooor.hold_THEEE_DOOOoooR and not Hold_The_Dooor.hOOOOooooOOOld_THEEE_DOOOoooR:
        Holddedoor(-20)


def Holdedddoorrr(HodoRRRRROOOOORRRRRRRRrrrr):
    global Hold_The_Dooor
    if Hold_The_Dooor.hold_THEEE_DOOOoooR and not Hold_The_Dooor.HOLddd_DOOOOOooRr and Hold_The_Dooor.HodoRRRRROOOOORRRRRRRRrrrr == HodoRRRRROOOOORRRRRRRRrrrr:
        Hold_dedoor()
        ODEODOR()
        Hodor.after(50, Holdedddoorrr, HodoRRRRROOOOORRRRRRRRrrrr)


def hOOOOooOOOOooOOOld_THEeE_DOOOoooOR(event):
    global Hold_The_Dooor

    if Hold_The_Dooor.hold_THEEE_DOOOoooR and not Hold_The_Dooor.HOldorR.hhhoooldDEEEEEEEEdoor == 0:
        Hold_The_Dooor.pause_pressed()


class HOldorR:
    def __init__(self):
        self.hoddor = OLDEDOOR[0] + OLDEDOOR[1]//2
        self.hodoorr = OHLDEDOOR[1] - 40
        self.img = PhotoImage(file='img/student_40x100.gif')
        self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)
        self.hhhoooldDEEEEEEEEdoor = 3

    def explod(self):
        Hooold_The_Door.delete(self.HODOOORHODORho)

    def revive(self):
        global Hold_The_Dooor
        self.hoddor = OLDEDOOR[0] + OLDEDOOR[1]//2
        self.hodoorr = OHLDEDOOR[1] - 40
        Hooold_The_Door.delete(self.HODOOORHODORho)
        self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)
        self.hhhoooldDEEEEEEEEdoor -= 1
        Hold_Theee_Door.configure(text="Vies : " + str(Hold_The_Dooor.HOldorR.hhhoooldDEEEEEEEEdoor), font=('Fixedsys', 16))
        Hold_The_Dooor.launch_animation()

    def redraw(self):
        Hooold_The_Door.delete(self.HODOOORHODORho)
        self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)


class Enemy:
    def __init__(self):
        self.hoddor = random.randint(OLDEDOOR[0]+10, OLDEDOOR[1]-10)
        self.hodoorr = random.randint(OHLDEDOOR[0]+10, OHLDEDOOR[1]//4)
        self.HODOOORHODORho = None
        self.type = "default"
        self.text = ["", "", ""]
        self.img = None
        self.set_body()

    def set_body(self):
        self.HODOOORHODORho = Hooold_The_Door.create_rectangle( self.hoddor + 60, self.hodoorr + 20, fill='blue')

    def explod(self):
        global Hold_The_Dooor
        Hooold_The_Door.delete(self.HODOOORHODORho)
        Hold_The_Dooor.hOOOOooooOOOld_THEEE_DOOOoooR = True
        Hold_The_Dooor.stop_animation()
        messagebox.showinfo("Info", self.message(HOOOoooOOldDDDdOOR=Hold_The_Dooor.HOOOoooOOldDDDdOOR))
        Hold_The_Dooor.hOOOOooooOOOld_THEEE_DOOOoooR = False
        Hold_The_Dooor.launch_animation()

    def redraw(self):
        Hooold_The_Door.delete(self.HODOOORHODORho)
        self.HODOOORHODORho = []
        self.set_body()

    def message(self, HOOOoooOOldDDDdOOR):
        return self.text[HOOOoooOOldDDDdOOR]


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
            self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)


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
            self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)


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
            self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)


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
            self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)


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
            self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)


class HolDDoooorr:
    """
    """
    def __init__(self, hoddor, hodoorr):
        self.hoddor = hoddor
        self.hodoorr = hodoorr
        self.img = PhotoImage(file='img/book_40x40.gif')
        self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)
        self.hodoorrRrrRrr = Holdddoor

    def explod(self):
        global Hold_The_Dooor
        Hooold_The_Door.delete(self.HODOOORHODORho)
        Hold_The_Dooor.holDDoooorrr.reHolddedoor(self)

    def Holddedoor(self):
        self.hodoorr -= self.hodoorrRrrRrr
        if self.hodoorr <= OHLDEDOOR[0]:
            self.explod()
        else:
            self.redraw()

    def redraw(self):
        Hooold_The_Door.delete(self.HODOOORHODORho)
        self.HODOOORHODORho = Hooold_The_Door.create_image(self.hoddor, self.hodoorr, image=self.img)


class HOOOOolDDoooorrrRRRR:
    """
    """
    def __init__(self, hoddor, hodoorr):
        self.hoddor = hoddor
        self.hodoorr = hodoorr
        self.HODOOORHODORho = Hooold_The_Door.create_oval(self.hoddor, self.hodoorr, self.hoddor + 4, self.hodoorr + 20, fill='orange')
        self.hodoorrRrrRrr = HoOdDedoor_Holdddoor

    def explod(self):
        global Hold_The_Dooor
        Hooold_The_Door.delete(self.HODOOORHODORho)
        Hold_The_Dooor.HoOdDedoor_holDDoooorr.reHolddedoor(self)

    def Holddedoor(self):
        self.hodoorr += self.hodoorrRrrRrr
        if self.hodoorr >= OHLDEDOOR[1]:
            self.explod()
        else:
            self.redraw()

    def redraw(self):
        Hooold_The_Door.delete(self.HODOOORHODORho)
        self.HODOOORHODORho = Hooold_The_Door.create_oval(self.hoddor, self.hodoorr, self.hoddor + 4, self.hodoorr + 20, fill='orange')


class Hold_The_Dooor:
    """

    """
    def __init__(self):
        self.hold_THEEE_DOOOoooR = False
        self.HOLddd_DOOOOOooRr = False
        self.holdDeDOoOOOOOOrRRRrrr = 0
        self.HOOOoooOOldDDDdOOR = 0
        self.HOldorR = HOldorR()
        self.holDDoooorrr = []
        self.HoOdDedoor = []
        self.HoOdDedoor_holDDoooorr = []
        self.hOOOOooooOOOld_THEEE_DOOOoooR = False
        self.paused_body = None
        self.HodoRRRRROOOOORRRRRRRRrrrr = 0

    def init_board(self):
        Hooold_The_Door.delete(ALL)
        self.holdDeDOoOOOOOOrRRRrrr = 0
        self.HOldorR = HOldorR()
        self.holDDoooorrr = []
        self.HoOdDedoor = []
        self.HoOdDedoor_holDDoooorr = []
        self.generate_HoOdDedoor()

        Hold_The_Doooor.configure(text="Score : " + str(self.holdDeDOoOOOOOOrRRRrrr))
        Hold_Theee_Door.configure(text="Vies : " + str(self.HOldorR.hhhoooldDEEEEEEEEdoor))

        self.hold_THEEE_DOOOoooR = True
        self.hOOOOooooOOOld_THEEE_DOOOoooR = False
        self.HOLddd_DOOOOOooRr = False
        self.launch_animation()

    def generate_HoOdDedoor(self):
        self.HoOdDedoor.append(Loyer())
        self.HoOdDedoor.append(MST())
        self.HoOdDedoor.append(Paperasse())
        self.HoOdDedoor.append(Alcool())
        self.HoOdDedoor.append(Drogue())

    def launch_Holdedddoorrr(self):
        self.HodoRRRRROOOOORRRRRRRRrrrr += 1
        Hodor.after(1000, HOOldedoor, self.HodoRRRRROOOOORRRRRRRRrrrr)
        Holdedddoorrr(self.HodoRRRRROOOOORRRRRRRRrrrr)

    def stop_animation(self):
        self.HOLddd_DOOOOOooRr = True

    def launch_animation(self):
        self.HOLddd_DOOOOOooRr = False
        self.launch_Holdedddoorrr()

    def pause_pressed(self):
        if self.hOOOOooooOOOld_THEEE_DOOOoooR:
            self.hOOOOooooOOOld_THEEE_DOOOoooR = False
            Hooold_The_Door.delete(self.paused_body)
            self.launch_animation()
        else:
            self.hOOOOooooOOOld_THEEE_DOOOoooR = True
            self.paused_body = Hooold_The_Door.create_text(320, 240, font=('Fixedsys', 18), text="PAUSE")
            self.stop_animation()


if __name__ == "__main__":
    Holdoor = 480
    Holdooor = 630
    Holdoooor = 5
    OLDEDOOR = [Holdoooor, Holdoor-Holdoooor]
    OHLDEDOOR = [Holdoooor, Holdooor-Holdoooor]

    HoOdDedoor = 4
    Hollldedoor = 3
    HoOdDedoor_Holdddoor = 3
    Holdddoor = 10

    Hodor = Tk()

    Hodor.title('University Invaders')

    Hooold_The_Door = Hooold_The_Door(Hodor, Holdoor=Holdoor, Holdooor=Holdooor, bg='black')


    Hooold_The_Door.bind_all("<Right>", Holdedddoor)
    Hooold_The_Door.bind_all("<Left>", Holdedddoorr)
    Hooold_The_Door.bind_all("<space>", HOLDEDOOR)
    Hooold_The_Door.bind_all("<p>", hOOOOooOOOOooOOOld_THEeE_DOOOoooOR)

    Hooold_The_Door.grid(row=1, column=0, columnspan=2, rowspan=3)

    Button(Hodor, text="Nouvelle partie", command=HHold_The_Dooor).grid(row=2, column=2, sticky=N, padx=5)
    Button(Hodor, text="Quitter", command=Hodor.destroy).grid(row=3, column=2, sticky=N, padx=5)


    Hold_The_Doooor=Label(Hodor, font=('Fixedsys', 16))
    Hold_Theee_Door=Label(Hodor, font=('Fixedsys', 16))
    Hold_The_Doooor.grid(row=0,column=0,sticky=W)
    Hold_Theee_Door.grid(row=0,column=1,sticky=E)

    Hoold_The_DOor = []

    if existe('HighScore')==0:
        HOOldoor=open('HighScore', 'w')
        pickle.dump(0,HOOldoor)
        HOOldoor.close()

    Hold_The_Dooor = Game()

    Hold_The_Door()

    Hodor.mainloop()
