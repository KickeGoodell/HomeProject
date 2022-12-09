import random                                                                                                                   
import pygame                                                                                                                   
from sys import exit                                                                                                            
from tkinter import *                                                                                                          
import tkinter as tk                                                                                                            
import mysql.connector                                                                                                          
#Importerer ulike systemer for å få koden min til å funke

def SqlConnect():                                                                                                               
    '''Funksjonen som gjør at du kan koble opp mot databasen'''                                                                 
    global conn                                                                                                                 # Globaliserer conn slik at den kan hentes inn og brukes i andre sammenhenger
    conn = mysql.connector.connect(                                                                                             # Variabel for å gjøre det enkelt å hente inn tilkoblingskommandoen senere i koden
        host="10.2.2.195",                                                                                                      # Ip-adresse til serveren
        user="enrique",                                                                                                         # Navn på bruker som skal tilkobles
        password="d9g[4k/Pphr10w00",                                                                                            # Passord på bruker som skal tilkobles
        database="Highscores"                                                                                                   # Navn på databasen som du skal koble til
    )                                                                                                                           


'''Globalisert variabler som brukes under hele koden og som ikke skal byttes'''                                                                                                                             
WIDTH = 500                                                                                                                     # Bredde på spillet
ROWS = 20                                                                                                                       # Hvor mange rader gridden i spillet består av
FBLUE = (11, 201, 205)                                                                                                          # Ulike farger som blir definert for bruk senere
FBLUEE =(20, 220, 220)                                                                                                          # Ulike farger som blir definert for bruk senere
FGREEN = (102,143,128)                                                                                                          # Ulike farger som blir definert for bruk senere
FYELLOW = (99,193,50)                                                                                                           # Ulike farger som blir definert for bruk senere


class Cube:                                                                                                                     
    '''Klasse som utgjør og lager start figuren i spillet'''                                                                    
    rows = ROWS                                                                                                                 # Hvilket rader som Cube klassen skal ta i utgangspunkt
    w = WIDTH                                                                                                                   # Hvilket størrelse på spillet som Cube klassen skal ta i utgangspunkt
    def __init__(self,start, dirnx=1, dirny=0, color=(FGREEN)):                                                                 
        '''Funksjon som skal kjøre i det programmet starter'''                                                                  
        self.pos = start                                                                                                        # Variabel med en parameter som definerer start posisjonen til snake figuren
        self.dirnx = dirnx                                                                                                      # Variabel med en parameter som definerer hvordan bevegelsense til snake utgjøres
        self.dirny = dirny                                                                                                      # Variabel med en parameter som definerer hvordan bevegelsense til snake utgjøres
        self.color = color                                                                                                      # Variabel med en parameter som definerer fargen til snake figuren


    def move(self,dirnx,dirny):                                                                                                 
        '''Funksjon som bestemmer hvordan figuren skal bevege seg'''                                                            
        self.dirnx = dirnx                                                                                                      # Variabel med en parameter som definerer hvordan bevegelsense til snake utgjøres
        self.dirny = dirny                                                                                                      # Variabel med en parameter som definerer hvordan bevegelsense til snake utgjøres
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)                                                         # Variabel med en parameter som definerer når snake figuren beveger på seg, så skal start posisjonen på figuren plusses med den nye posisjonen


    def draw(self, surface, eyes=False):                                                                                        
        '''Funksjon som bestemmer hvordan figuren fysisk ser ut, størrelse, farge og øyener'''                                  
        dis = self.w // self.rows                                                                                               # Variabel med en parameter som definerer distansen mellom hver x og y verdi, defineres som dis utføres av å dele posisjonen til snake figurens "i forhold til bredden av skjermen" sammen med posisjonen til snake figuren "i forhold til hvilket del av gridden"
        i = self.pos[0]                                                                                                         # Variabel med en parameter som definerer i er raden i gridden som finnes av posisjonen til snake figuren
        j = self.pos[1]                                                                                                         # Variabel med en parameter som definerer j er kolonne i gridden som finnes av posisjonen til snake figuren

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))                                     # En rektangel som blir laget i pygame som blir definert av en farge og en størrelse som er bestemt ovenfor

        if eyes:                                                                                                                # If statement som kjører øyenene
            centre = dis//2                                                                                                     # Variabel som definerer central punktet av hver objekt
            radius = 3 
            eyeColor = (0,0,0)                                                                                                  # Variabel som definerer radiusen til øynene
            circleMiddle = (i * dis + centre-radius, j * dis + 8)                                                               # Variabel som definerer første øyet
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)                                                           # Variabel som definerer andre øyet
            pygame.draw.circle(surface, eyeColor, circleMiddle, radius)                                                         # En sirkel som tegnes av pygame som tegnes da det første øyet, setter farge og deres størrelse
            pygame.draw.circle(surface, eyeColor, circleMiddle2, radius)                                                        # En sirkel som tegnes av pygame som tegnes da det andre øyet, setter farge og deres størrelse

class Snake:                                                                                                                                
    '''Funksjon som definerer og lager hele "snake" figuren som settes sammen etter du har spist "mat,                                                                                                                              
        samtidig bestemme hvordan du beveger deg og hvordan bitene settes sammen'''                                                                                                                             
    body = []                                                                                                                   # En array som lages for å kunne sette sammen de forskjellige objektene
    turns = {}                                                                                                                  # En array som lages for å kunne huske grad posisjonene du flytter snake figuren


    def __init__(self, color, pos):                                                                                                                             
        '''Funksjon som kjører i det programmet starter, som bestemmer hoden og bitene som skal legges på  i etterkant'''                                                                                                                               
        self.color = color                                                                                                      # Variabel med en parameter som definerer fargen på snake som hentes inn
        self.head = Cube(pos)                                                                                                   # Variabel med en parameter som definerer hoden til snake som hentes inn som start posisjonen til snake
        self.body.append(self.head)                                                                                             # Parameter som henter inn at hoden til snake skal legges inn først i body arrayen
        self.dirnx = 0                                                                                                          # Variabel med en parameter som definerer hvordan bevegelsense til snake utgjøres
        self.dirny = 1                                                                                                          # Variabel med en parameter som definerer hvordan bevegelsense til snake utgjøres


    def move(self):                                                                                                                            
        '''Funksjon som definerer hvordan du skal kunne bevege deg i spillet'''                                                 
        for event in pygame.event.get():                                                                                        # For loop som kjører hvergang noe skjer i pygame vinduet
            if event.type == pygame.QUIT:                                                                                       # If statement som kjører hvergang noe skjer i pygame vinduet, i dette tilfellet hvis du trykker på den røde lukk knappen
                pygame.quit()                                                                                                   # Kommandoen som skal lukke vinduet

            keys = pygame.key.get_pressed()                                                                                     # Variabel som definerer en liste med verdier når knapper trykkes i pygame

            if keys[pygame.K_a] and not self.dirnx == 1:                                                                        # If statement som kjører hvergang du trykker a, så skal noe skje og da kan du i tillegg ikke bevege deg andre veien
                self.dirnx = -1                                                                                                 # Variabel med en parameter som definerer x posisjonen til snake figuren
                self.dirny = 0                                                                                                  # Variabel med en parameter som definerer y posisjonen til snake figuren
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]                                                         # Variabel med en parameter som definerer hvilket posisjon snake figuren byttet posisjon og "husker" den posisjonen i en array

            elif keys[pygame.K_d] and not self.dirnx == -1:                                                                     # If statement som kjører hvergang du trykker d, så skal noe skje og da kan du i tillegg ikke bevege deg andre veien
                self.dirnx = 1                                                                                                  # Variabel med en parameter som definerer x posisjonen til snake figuren
                self.dirny = 0                                                                                                  # Variabel med en parameter som definerer y posisjonen til snake figuren
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]                                                         # Variabel med en parameter som definerer hvilket posisjon snake figuren byttet posisjon og "husker" den posisjonen i en array

            elif keys[pygame.K_w] and not self.dirny == 1:                                                                      # If statement som kjører hvergang du trykker w, så skal noe skje og da kan du i tillegg ikke bevege deg andre veien
                self.dirnx = 0                                                                                                  # Variabel med en parameter som definerer x posisjonen til snake figuren
                self.dirny = -1                                                                                                 # Variabel med en parameter som definerer y posisjonen til snake figuren
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]                                                         # Variabel med en parameter som definerer hvilket posisjon snake figuren byttet posisjon og "husker" den posisjonen i en array

            elif keys[pygame.K_s] and not self.dirny == -1:                                                                     # If statement som kjører hvergang du trykker s, så skal noe skje og da kan du i tillegg ikke bevege deg andre veien
                self.dirnx = 0                                                                                                  # Variabel med en parameter som definerer x posisjonen til snake figure
                self.dirny = 1                                                                                                  # Variabel med en parameter som definerer y posisjonen til snake figure
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]                                                         # Variabel med en parameter som definerer hvilket posisjon snake figuren byttet posisjon og "husker/kopierer" den posisjonen i en array

        for i, c in enumerate(self.body):                                                                                       # For loop som skal finne en verdi i en variabel med en parameter
            p = c.pos[:]                                                                                                        # Variabel som definerer posisjonen til alle cube objektene i programmet
            if p in self.turns:                                                                                                 # If statement som skal sjekke om posisjonen til cube objekten er den samme posisjonen som posisjonen i turns arrayen
                turn = self.turns[p]                                                                                            # Variabel som definerer den posisjnen til parameter posisjonen i turns arrayen
                c.move(turn[0], turn[1])                                                                                        # Hvis det ovenfor stemmer, så skal cube objektet flytte seg
                if i == len(self.body) - 1:                                                                                     # If statement som skal sjekke om indeksen til snu posisjonen er den samme som lengden på snake posisjonen - 1
                    self.turns.pop(p)                                                                                           # Hvis det ovenfor stemmer så skal den posisjonen i turns arrayen slettes
            else:                                                                                                               # Hvis det ovenfor i første if statement ikke stemmer så skal dette skje
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])                                                # If statement som skal sjekke om snake beveger seg til venstre og treffer enden av skjermen, hvis ja, så skal den dukke opp på høyre side av skjermen
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])                                                # Elif statement som skal sjekke om snake beveger seg til høyre og treffer enden av skjermen, hvis ja, så skal den dukke opp på venstre side av skjermen
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)                                               # Elif statement som skal sjekke om snake beveger seg nedover og treffer enden av skjermen, hvis ja, så skal den dukke opp på øverst side av skjermen
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)                                              # Elif statement som skal sjekke om snake beveger seg oppover og treffer enden av skjermen, hvis ja, så skal den dukke opp på nederste side av skjermen
                else: c.move(c.dirnx, c.dirny)                                                                                  # Hvis ingen av det ovenfor stemmer så skal snake eller cube objektene bare fortsette å bevege selg som vanlig


    def reset(self, pos):                                                                                                                               
        '''Funksjon som kjører når du starter spillet på nytt, som vil sette original figuren tilbake der den starter'''                                                                                                                                
        self.head = Cube(pos)                                                                                                   # Variabel med en parameter som definerer start posisjonen til snake figuren
        self.body = []                                                                                                          # Variabel med en parameter som definerer en array som skal sette sammen objektene
        self.body.append(self.head)                                                                                             # Parameter som henter inn at hoden til snake skal legges inn først i body arrayen
        self.turns = {}                                                                                                         # Variabel med en parameter som definerer en array som skal "huske" posisjonene til snake figuren hver gang den flytte seg i en annen akse 
        self.dirnx = 0                                                                                                          # Variabel med en parameter som definerer hvordan bevegelsense til snake utgjøres
        self.dirny = 1                                                                                                          # Variabel med en parameter som definerer hvordan bevegelsense til snake utgjøres


    def addCube(self):                                                                                                                              
        '''Funksjonen som bestemmer hvordan bitene settes sammen og hvor de legges'''                                                                                                                               
        tail = self.body[-1]                                                                                                    # Variabel som definerer body arrayen
        dirnx, dirny = tail.dirnx, tail.dirny                                                                                   # Variabel som definerer at dirnx, dirny er halen til snake figuren

        if dirnx == 1 and dirny == 0:                                                                                           # If statement som kjører hvergang snake figuren beveger seg til venstre
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))                                                              # Hvis ja, så legges på en cube objekt på siste posisjon av snake figuren -1 (positiv retning)
        elif dirnx == -1 and dirny == 0:                                                                                        # If statement som kjører hvergang snake figuren beveger seg til høyre
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))                                                              # Hvis ja, så legges på en cube objekt på siste posisjon av snake figuren +1 (negativ retning)
        elif dirnx == 0 and dirny == 1:                                                                                         # If statement som kjører hvergang snake figuren beveger seg nedover
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))                                                              # Hvis ja, så legges på en cube objekt på siste posisjon av snake figuren -1 (positiv retning)
        elif dirnx == 0 and dirny == -1:                                                                                        # If statement som kjører hvergang snake figuren beveger seg oppover
            self.body.append(Cube((tail.pos[0], tail.pos[1] +1)))                                                               # Hvis ja, så legges på en cube objekt på siste posisjon av snake figuren +1 (negativ retning)

        self.body[-1].dirnx = dirnx                                                                                             # Variabel med en array som definerer at den nye cube objekten beveger seg i samme retning som hele snake figuren (x aksen i dette tilfellet)
        self.body[-1].dirny = dirny                                                                                             # Variabel med en array som definerer at den nye cube objekten beveger seg i samme retning som hele snake figuren (y aksen i dette tilfellet)


    def draw(self, surface):      
        '''Funksjon som definerer hvilket cube objekter skal ha øyener og hvilker skal ikke'''                                                                                              
        for i, c in enumerate(self.body):                                                                                       # For løkke som skal finne en verdi i en variabel med en parameter
            if i == 0:                                                                                                          # Hvis indeks til snake kroppen er 0
                c.draw(surface, True)                                                                                           # Så skal cube objekten lages med øyner
            else:                                                                                                               # Hvis ikke
                c.draw(surface)                                                                                                 # Så skal cube objekten bare lages


def drawGrid(w, rows, surface):                                                                                                 
    '''Funksjon som lager og "tegner" gridden i spillet som gjør det enklere for "snake" å bevege seg,                          
        samtidig mat som plasseres'''                                                                                           
    sizeBtwn = w // rows                                                                                                        # Variabel som definerer hvor stor mellom det skal være mellom hver rad og kolonne i gridden 

    x = 0                                                                                                                       # Variabel som definerer x graden til gridden
    y = 0                                                                                                                       # Variabel som definerer y graden til gridden
    for l in range(rows):                                                                                                       # For løkke som kjører selve konstruksjonen av gridden
        x = x + sizeBtwn                                                                                                        # Setter x graden til å være x variabelen + størrelsen på mellomrommet i gridden
        y = y + sizeBtwn                                                                                                        # Setter y graden til å være y variabelen + størrelsen på mellomrommet i gridden

        pygame.draw.line(surface, (FBLUEE), (x,0) , (x, w))                                                                     # Linje som blir laget for å definere gridden, med farge, start og slutt posisjon for den vertikale linjen
        pygame.draw.line(surface, (FBLUEE), (0,y) , (w, y))                                                                     # Linje som blir laget for å definere gridden, med farge, start og slutt posisjon for den horisontale linjen


def redrawWindow(surface):                                                                                                      
    '''Funksjom som laster vinduet på nytt hver gang du beveger på deg eller spiser mat'''                                      
    global s, snack                                                                                                             # Globaliserer s og snack slik at de kan brukes i andre sammenhenger
    surface.fill((FBLUE))                                                                                                       # Gjør vinduet til et bestemt farge
    s.draw(surface)                                                                                                             # Kaller inn draw funksjonen fra snake klassen som blir definert tidligere i programmet
    snack.draw(surface)                                                                                                         # Kaller inn draw funksjonen fra snack variablen som blir definert senere i programmet
    drawGrid(WIDTH, ROWS, surface)                                                                                              # Kjører funksjonen drawGrid som lagre gridden i skjermen
    pygame.display.set_caption(f"Din score: {len(s.body)}")                                                                     # Titell på vinduet som lages i pygame
    pygame.display.update()                                                                                                     # Oppdaterer skjermen i pygame


def randomSnack(rows, item):                                                                                                    
    '''Funksjon som lager tilfeldig mat som "spawnes" overalt på mappet'''                                                      
    positions = item.body                                                                                                       # Variabel som definerer en liste

    while True:                                                                                                                 # While løkke som skal kjøre hele tiden
        x = random.randrange(rows)                                                                                              # Variabel som definerer et innebygd python funksjon så innlegger bestemte elementer på et bestemt sted (mat, og x aksen i dette tilfellet)
        y = random.randrange(rows)                                                                                              # Variabel som definerer et innebygd python funksjon så innlegger bestemte elementer på et bestemt sted (mat, og y aksen i dette tilfellet)
        if len(list(filter(lambda z:z.pos == (x,y) , positions))) > 0:                                                          # If statement som finner ut om posisjonen til der maten skal innlegges er det samme som posisjonen til snake figuren så skal noe skje
            continue                                                                                                            # Hvis if statementet stemmer, så skal det kjøres på nytt
        else:                                                                                                                   # Hvis ikke så skal while loop stoppes
            break                                                                                                               # Stopper while løkke

    return (x, y)                                                                                                               # Returnere x og y variabelene


def mainMessageWindow():
    '''Funksjon som kjører hoved vinduet i det du dør i spillet, som inneholder en meny og valg''' 
    mainWin = Tk()                                                                                                              # Variabel som definerer tkinter vinduet som mainWin
    mainWin.title(f"Du døde... Din score ble: {len(s.body)}")                                                                   # Titell på vinduet som blir laget i tkinter
    mainWin.geometry('400x200')                                                                                                 # Definerer størrelsen på vinduet som lages i tkinter
    message = "Vil du lagre highscoren, avslutt, prøv på nytt eller vis leaderboard?"                                           # Variabel som definerer hva som skal være meldingen
    Label(mainWin,text=message).pack()                                                                                          # En tekst element som legges over knappene i tkinter vinduet
    Button(mainWin, text='Lagre', command=saveWindow).pack()                                                                    # Knapp som lages av tkinter som har teksten Save og kjører "saveWindow" funksjonen når den trykkes
    Button(mainWin, text='Avslutt', command=exit).pack()                                                                        # Knapp som lages av tkinter som har teksten Quit og kjører "quit" funksjonen når den trykkes
    Button(mainWin, text='Prøv På Nytt', command=mainWin.destroy).pack()                                                        # Knapp som lages av tkinter som har teksten Play Again og kjører "mainWin.destroy" funksjonen når den trykkes
    Button(mainWin, text='Vis Leaderboard', command=showLeaderboard).pack()                                                     # Knapp som lages av tkinter som har teksten Show Leaderboard og kjører "showLeaderboard" funksjonen når den trykkes
    mainWin.mainloop()                                                                                                          # Kaller tilbake tkinter vinduet


def saveWindow():
    '''Funksjon som kjører et vindu som er koblet opp mot databasen slik at du kan lagre innhold til databasen'''

    saveWin = Tk()                                                                                                              # Variabel som definerer tkinter vinduet som saveWin
    saveWin.title('Lagre Highscore')                                                                                            # Titell på vinduet som blir laget i tkinter
    saveWin.geometry('400x200')                                                                                                 # Definerer størrelsen på vinduet som lages i tkinter
    message = "Skriv inn navnet ditt!"                                                                                          # Variabel som definerer hva som skal være meldingen
    Label(saveWin, text=message).pack()                                                                                         # En tekst element som legges over tekstboksen i tkinter vinduet
    inputtxt = tk.Text(saveWin, height = 5, width = 20)                                                                         # Variable som definerer og lager tekstboksen i tkinter vinduet
    inputtxt.pack()                                                                                                             # Kaller inn fuksjonen pack() som gjør den viselig på skjermen


    def save():
        '''Funksjon som kjører selve infomasjons lagringen i databasen'''
        SqlConnect()                                                                                                            # Funksjonen som defineres over, men er koblingen til databasen
        cursor = conn.cursor()                                                                                                  # Variabel som definerer kommandoen som brukes senere
        inputtxtget = inputtxt.get(1.0, "end-1c")                                                                               # Denne variabelen henter inn innholdet du leggger inn i tekst feltet som da blir brukt senere til å lagres inn i databasen
        query = f"INSERT INTO Attempts (Navn, Score, Dato) VALUES ('{inputtxtget}', {len(s.body)}, CURDATE())"                   # Variable som defineres hvilket informasjon som skal innhentes eller sendes til/fra databasen,

        cursor.execute(query)                                                                                                   # Kommando som kjører variabelen "query"
        conn.commit()                                                                                                           # Kommando som lagrer og gjør endringene permanent i databasen

        saveWin.destroy()                                                                                                       # Ødelegger det vinduet i det den er ferdig med å lagre informasjonen til databasen

    Button(saveWin, text='Lagre', command=save).pack()                                                                           # Knapp som lages av tkinter som har teksten save og kjører "save" funksjonen når den trykkes
    
    
def showLeaderboard():
    '''Funksjon som kobler seg opp mot databasen og viser deg informasjon fra databasen'''
    leaderboardWin = tk.Tk()                                                                                                    # Variabel som definerer tkinter vinduet som leaderboardWin
    leaderboardWin.geometry("400x200")                                                                                          # Definerer størrelsen på vinduet som lages i tkinter

    SqlConnect()                                                                                                                # Funksjon som defineres over, men er koblingen til databasen
    cursor = conn.cursor()                                                                                                      # Variabel som definerer kommandoen som brukes senere
    query = "SELECT Navn, Score, DATE_FORMAT(Dato, '%d.%m.%Y') Dato FROM Attempts ORDER BY Score DESC LIMIT 0,5 "                # Variabel som defineres hvilket informasjon som skal innhentes eller sendes til/fra databasen, 
                                                                                                                                # i tillegg putter den i rekkefølge og limiterer hvor mye som skal vises
    cursor.execute(query)                                                                                                       # Kommando som kjører variabelen "query"

    e = Label(leaderboardWin, width = 10, text = "Navn",borderwidth = 2, relief = 'ridge', anchor = 'w') 
    e.grid(row=0, column=0)
    e = Label(leaderboardWin, width = 10, text = "Score",borderwidth = 2, relief = 'ridge', anchor = 'w') 
    e.grid(row=0, column=1)
    e = Label(leaderboardWin, width = 10, text = "Dato",borderwidth = 2, relief = 'ridge', anchor = 'w') 
    e.grid(row=0, column=2)   
    i=1                                                                                                                         
    # Kommandoer som lager en liten tabel øverst på tkinter boksen som legger in navn, plassering, farge og design

    for Attempts in cursor:                                                                                                      # For løkke som sjekker etter informasjon inn i tabelen inn på daabasen
        for j in range(len(Attempts)):                                                                                           # For hvergang den finner informasjon skal den legges inn på et tabell som er laget i tkinter
            e = Label(leaderboardWin, width = 10, text = Attempts[j],borderwidth = 2, relief = 'ridge', anchor = 'w')            # Kommando som lager tabellen som legges inn på tkinter boksen som bestemmer, innhold, plassering, farge og design
            e.grid(row=i, column=j)                                                                                             # Tabellen sin definisjon
        i=i+1                                                                                                                   
        #Etter den går gjennom første indeksen, skal den plusses på en å gjør det samme igjen

    noe = Button(leaderboardWin, text='Lukk Vinduet', command=leaderboardWin.destroy)
    noe.grid(row = 6 , column = 1)


def main():
    '''Hovedfunksjonen som kjører spillet i sin helhet'''
    global s, snack                                                                                                             # Globaliserer s og snake slik at den kan brukes i andre sammenhenger

    s = Snake((FGREEN), (10, 10))                                                                                               # Variabel som definerer "snake" som s som hentes inn fra "snake" klassen, deretter gir den en farge og en start posisjon
    snack = Cube(randomSnack(ROWS, s), color = (FYELLOW))                                                                       # Variabel som definerer randomsnack funksjonen som snack som hentes inn fra "Cube" klassen, deretter kaller randomSnack funksjonen og til slutt gir den en størrelse og farge
    win = pygame.display.set_mode((WIDTH, WIDTH))                                                                               # Variabel som definerer størreslen på vinduet i pygame og blir tilkalt som win
    flag = True                                                                                                                 # Setter flag while løkken til true slik at løkken kjører
    clock = pygame.time.Clock()                                                                                                 # Variabel som defineres som clock som utgjør hvor raskt programmet skal kjøres     

    while flag:                                                                                         
        '''While løkke som kjører spillet'''
        pygame.time.delay(50)                                                                                                   # Kommando som slakner spillet et halv sekund slik at den ikke kjører i 10fps nøyaktig
        clock.tick(10)                                                                                                          # Kommando som utgjør hastigheten til spillet, i dette tilfellet så er det 10fps

        s.move()                                                                                                                # Kaller inn move funksjonen som blir definert i snake klassen tidligere i programmet
        if s.body[0].pos == snack.pos:                                                                                          # En if statement som kjører hvergang "snake spiser mat" i dette tilfellet skal den legge på en figure og "spawne" en ny matbit
            s.addCube()                                                                                                         # Kaller "addCube" funksjonen som blir definert tidligere i programmet
            snack = Cube(randomSnack(ROWS, s), color = (FYELLOW))                                                               # Variabel som definerer matbiten med størrelse og farge

        for x in range(len(s.body)):                                                                                            # For løkke som skjekker alle posisjonene i hele snake figuren
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):                                                        # If statement som kjører hvergang posisjonen som snake figuren beveger seg i er dem samme posisjonen som resten av kroppen på snak figuren
                mainMessageWindow()                                                                                             # Hvis ja, så skal denne funksjonen kjøres
                s.reset((10, 10))                                                                                               # Deretter skal denne funksjonen kjøres med en start posisjon
                break                                                                                                           # Og deretter skal For løkken avsluttes

        redrawWindow(win)                                                                                                       # Kaller inn redrawWindow funksjonen som blir definert tidligere i programmet

main()                                                                                                                          # Kaller tilbake funksjonen main

