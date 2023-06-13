import random                                                                                                                   
import pygame                                                                                                                   
from sys import exit                                                                                                            
from tkinter import *                                                                                                          
import tkinter as tk                                                                                                            
import mysql.connector                                                                                                          
#Importing different systems to ensure functionality in my code

def SqlConnect():                                                                                                               
    '''Function that establishes connection to the database'''                                                                 
    global conn                                                                                                                 # Globalizes conn so that it can be reused in other scenarios
    conn = mysql.connector.connect(                                                                                             # Variable made to make it easier to get the connection command later
        host="10.2.2.195",                                                                                                      # Ip-adresse to the server
        user="enrique",                                                                                                         # Navn på bruker som skal tilkobles Name of user that is being connected to
        password="d9g[4k/Pphr10w00",                                                                                            # Passord on the user thats being connected to
        database="HomeProject"                                                                                                   # Name to the database that is being connected to
    )                                                                                                                           


'''Globalized variables which are used under the entire program and shall not be changed'''                                                                                                                             
WIDTH = 500                                                                                                                     # Width of the game
ROWS = 20                                                                                                                       # How many rows the grid is based off of
FBLUE = (11, 201, 205)                                                                                                          # Color variables that are being defined and used later
FBLUEE =(20, 220, 220)                                                                                                          # Color variables that are being defined and used later
FGREEN = (102,143,128)                                                                                                          # Color variables that are being defined and used later
FYELLOW = (99,193,50)                                                                                                           # Color variables that are being defined and used later


class Cube:                                                                                                                     
    '''Class that defines and creates the start position for the figure in the game'''                                                                    
    rows = ROWS                                                                                                                 # Which rows that the cube class is supposed to use
    w = WIDTH                                                                                                                   # Which size of the game that the cube class is supposed to use
    def __init__(self,start, dirnx=1, dirny=0, color=(FGREEN)):                                                                 
        '''Function that runs when the program starts which places the snake in its first position'''                                                                  
        self.pos = start                                                                                                        # Variable with a parameter which defines the start position to the snake figure
        self.dirnx = dirnx                                                                                                      # Variable with a parameter which defines the start movements to the snake figure
        self.dirny = dirny                                                                                                      # Variable with a parameter which defines the start movements to the snake figure
        self.color = color                                                                                                      # Variable with a parameter which defines the colors to the snake figure


    def move(self,dirnx,dirny):                                                                                                 
        '''Function that decides how the figure moves'''                                                            
        self.dirnx = dirnx                                                                                                      # Variable with a parameter which defines the movements to the snake figure
        self.dirny = dirny                                                                                                      # Variable with a parameter which defines the movements to the snake figure
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)                                                         # Variable with a parameter which defines when the snake figure moves, then the start position plusses with the new position


    def draw(self, surface, eyes=False):                                                                                        
        '''Function that decides how the figure will look physically. Size, color and eyes are defined here'''                                  
        dis = self.w // self.rows                                                                                               # Variable with a parameter which defines the distance between each x and y vaulue, defines those as dis, is done by devided the position of the snake figure "in corrolation to the width of the screen" together with the position of the snake figure "in corrolation to each piece of the grid"
        i = self.pos[0]                                                                                                         # Variable with a parameter which defines "i" which is the row in the grid which is found by the position of the snake figure
        j = self.pos[1]                                                                                                         # Variable with a parameter which defines "j" which is the column in the grid which is found by the position of the snake figure

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))                                     # A rectanlge which is being made in pygame which is defined by a color and a size which is defined above

        if eyes:                                                                                                                # If statement which runes the eyes
            centre = dis//2                                                                                                     # Variable that defines the central point of each object
            radius = 3 
            eyeColor = (0,0,0)                                                                                                  # Variable which defines the radius to the eyes 
            circleMiddle = (i * dis + centre-radius, j * dis + 8)                                                               # Variable which defines the first eye 
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)                                                           # Variable which defines the second eye
            pygame.draw.circle(surface, eyeColor, circleMiddle, radius)                                                         # A circle which is made in pygame which draws the first eye, sets the color and its size
            pygame.draw.circle(surface, eyeColor, circleMiddle2, radius)                                                        # A circle which is made in pygame which draws the second eye, sets the color and its size

class Snake:                                                                                                                                
    '''Funksjon som definerer og lager hele "snake" figuren som settes sammen etter du har spist "mat,                                                                                                                              
    samtidig bestemme hvordan du beveger deg og hvordan bitene settes sammen'''                                                                                                                             
    body = []                                                                                                                   # An array which is made to put together the different objects
    turns = {}                                                                                                                  # An array which is made to remember the degree positions you move the snake figure


    def __init__(self, color, pos):                                                                                                                             
        '''Function that runs when the program starts, this function defines the head 
        and where the pieces are place afterwards'''                                                                                                                               
        self.color = color                                                                                                      # Variable with a parameter which defines the color on the snake figure thats being recieved
        self.head = Cube(pos)                                                                                                   # Variable with a parameter which defines the head to the snake which gets the start position to the snake
        self.body.append(self.head)                                                                                             # Parameter which gets the head to the snake and puts it first in the body array
        self.dirnx = 0                                                                                                          # Variable with a parameter which defines the movements to the snake figure
        self.dirny = 1                                                                                                          # Variable with a parameter which defines the movements to the snake figure


    def move(self):                                                                                                                            
        '''Function that defines how you move in the game'''                                                 
        for event in pygame.event.get():                                                                                        # For loop which runs every time something happens in the pygame window
            if event.type == pygame.QUIT:                                                                                       # If statement which runs every time something happens in the pygame window, in this case if you press the red close button
                pygame.quit()                                                                                                   # Command to close the window

            keys = pygame.key.get_pressed()                                                                                     # Variable which defines a list of values when the buttons are pressed in pygame 

            if keys[pygame.K_a] and not self.dirnx == 1:                                                                        # If statement which runs everytime you press a, then somehting is supposed to happen in addition to you not being able to move the other direction
                self.dirnx = -1                                                                                                 # Variable with a parameter which defines the x position to the snake figure
                self.dirny = 0                                                                                                  # Variable with a parameter which defines the y position to the snake figure
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]                                                         # Variable with a parameter which defines which position the snake figure changed and "remembers" this position in an array

            elif keys[pygame.K_d] and not self.dirnx == -1:                                                                     # If statement which runs everytime you press d, then somehting is supposed to happen in addition to you not being able to move the other direction
                self.dirnx = 1                                                                                                  # Variable with a parameter which defines the x position to the snake figure
                self.dirny = 0                                                                                                  # Variable with a parameter which defines the y position to the snake figure
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]                                                         # Variable with a parameter which defines which position the snake figure changed and "remembers" this position in an array

            elif keys[pygame.K_w] and not self.dirny == 1:                                                                      # If statement which runs everytime you press w, then somehting is supposed to happen in addition to you not being able to move the other direction
                self.dirnx = 0                                                                                                  # Variable with a parameter which defines the x position to the snake figure
                self.dirny = -1                                                                                                 # Variable with a parameter which defines the y position to the snake figure
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]                                                         # Variable with a parameter which defines which position the snake figure changed and "remembers" this position in an array

            elif keys[pygame.K_s] and not self.dirny == -1:                                                                     # If statement which runs everytime you press s, then somehting is supposed to happen in addition to you not being able to move the other direction
                self.dirnx = 0                                                                                                  # Variable with a parameter which defines the x position to the snake figure
                self.dirny = 1                                                                                                  # Variable with a parameter which defines the y position to the snake figure
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]                                                         # Variable with a parameter which defines which position the snake figure changed and "remembers" this position in an array

        for i, c in enumerate(self.body):                                                                                       # For loop thats finding a value with a parameter 
            p = c.pos[:]                                                                                                        # Variable that defines the position to all the cube objects in the program 
            if p in self.turns:                                                                                                 # If statement that checks if the position to the cube object is the same as the positon thats "remembered" in the turns array
                turn = self.turns[p]                                                                                            # Variable that defines the position to the parameter position in the turns array 
                c.move(turn[0], turn[1])                                                                                        # If above is correct then the cube object moves
                if i == len(self.body) - 1:                                                                                     # If statement that checks if the index to the turn position is the same as the length of the snake -1 
                    self.turns.pop(p)                                                                                           # If what above is correct then the position in the turns array is deleted
            else:                                                                                                               # If what above in the first if statement isn't true then this is supposed to happen 
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])                                                # If statement that checks if the snake moves to the left and hits the end of the screen, if so then the figure shows up on the right side of the screen 
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])                                                # Elif statement that checks if the snake moves to the right and hits the end of the screen, if so then the figure shows up on the left side of the screen
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)                                               # Elif statement that checks if the snake moves to the bottom and hits the end of the screen, if so then the figure shows up on the top side of the screen
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)                                              # Elif statement that checks if the snake moves to the top and hits the end of the screen, if so then the figure shows up on the bottom side of the screen
                else: c.move(c.dirnx, c.dirny)                                                                                  # If none of the above is true, then the snake or the cube objects keep moving themselves as normal


    def reset(self, pos):                                                                                                                               
        '''Function that runs when you restart the game, this will set the original 
        figure back where it started originally'''                                                                                                                                
        self.head = Cube(pos)                                                                                                   # Variable with a parameter that defines the start position to the snake figure
        self.body = []                                                                                                          # Variable with a parameter that defines an array which puts together the objects
        self.body.append(self.head)                                                                                             # Parameter that gets the head of the snake and places it first in the body array
        self.turns = {}                                                                                                         # Variable with a parameter that defines an array which will "remember" the positions to the snake figure every time it moves to a different axis 
        self.dirnx = 0                                                                                                          # Variable with a parameter which defines the movements to the snake figure
        self.dirny = 1                                                                                                          # Variable with a parameter which defines the movements to the snake figure


    def addCube(self):                                                                                                                              
        '''Function that decides how the pieces of snake fit together and where they are supposed to be placed'''                                                                                                                               
        tail = self.body[-1]                                                                                                    # Variable that defines the body array
        dirnx, dirny = tail.dirnx, tail.dirny                                                                                   # Variable that defines that dirnx and dirny is the tail to the snake figure

        if dirnx == 1 and dirny == 0:                                                                                           # If statement that runs everytime the snake figure moves to the left
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))                                                              # If so, then it adds a cube object on the last position of the snake figure -1 (positiv direction)
        elif dirnx == -1 and dirny == 0:                                                                                        # If statement that runs everytime the snake figure moves to the right
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))                                                              # If so, then it adds a cube object on the last position of the snake figure +1 (negative direction)
        elif dirnx == 0 and dirny == 1:                                                                                         # If statement that runs everytime the snake figure moves upwards
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))                                                              # If so, then it adds a cube object on the last position of the snake figure -1 (positiv direction)
        elif dirnx == 0 and dirny == -1:                                                                                        # If statement that runs everytime the snake figure moves downwards
            self.body.append(Cube((tail.pos[0], tail.pos[1] +1)))                                                               # If so, then it adds a cube object on the last position of the snake figure +1 (negative direction)

        self.body[-1].dirnx = dirnx                                                                                             # Variable with an array that defines that the new cube object moves in the same direction as the whole snake figure (x axis in this scenario)
        self.body[-1].dirny = dirny                                                                                             # Variable with an array that defines that the new cube object moves in the same direction as the whole snake figure (y axis in this scenario)


    def draw(self, surface):      
        '''Function that defines which cube objects will have eyes and which shall not'''                                                                                              
        for i, c in enumerate(self.body):                                                                                       # For loop that finds a variable with a parameter  
            if i == 0:                                                                                                          # If the index to the snake body varible it found is 0
                c.draw(surface, True)                                                                                           # Then the cube object is made with eyes
            else:                                                                                                               # If not
                c.draw(surface)                                                                                                 # Then the cube object is created


def drawGrid(w, rows, surface):                                                                                                 
    '''Function that creates and draws the grid in the game. This is neccesarry to make it easier for the snake,
    to move around as well as food is placed'''                                                                                           
    sizeBtwn = w // rows                                                                                                        # Variable that defines how big the space between the row and column is in the grid

    x = 0                                                                                                                       # Variable that defines the x degree to the grid
    y = 0                                                                                                                       # Variable that defines the y degree to the grid
    for l in range(rows):                                                                                                       # For loop which runs the creation of the grid
        x = x + sizeBtwn                                                                                                        # Sets the x degree to be the x variable + the size of the space between in the grid
        y = y + sizeBtwn                                                                                                        # Sets the y degree to be the y variable + the size of the space between in the grid

        pygame.draw.line(surface, (FBLUEE), (x,0) , (x, w))                                                                     # Line made to define the grid, with color, start and end position for the vertical line
        pygame.draw.line(surface, (FBLUEE), (0,y) , (w, y))                                                                     # Line made to define the grid, with color, start and end position for the vertical line


def redrawWindow(surface):                                                                                                      
    '''Function that reloads the window everytime you move or eat food'''                                      
    global s, snack                                                                                                             # Globalises s and snack so that they can be used later on
    surface.fill((FBLUE))                                                                                                       # Makes the window a specific color
    s.draw(surface)                                                                                                             # Calls in the draw function from the snake class that was defined earlier
    snack.draw(surface)                                                                                                         # Calls in the draw function from the snack variable that is defined later
    drawGrid(WIDTH, ROWS, surface)                                                                                              # Runs the function drawGrid which makes the grid in the screen
    pygame.display.set_caption(f"Your score {len(s.body)}")                                                                     # The window title that's made in pygame
    pygame.display.update()                                                                                                     # Updates the screen in pygame


def randomSnack(rows, item):                                                                                                    
    '''Function that creates the food that is spawned randomly on the field'''                                                      
    positions = item.body                                                                                                       # Variable that defines a list

    while True:                                                                                                                 # While loop that is going to run all the time
        x = random.randrange(rows)                                                                                              # Variable that defines a built in python function that places specific elements at random places (food and the x axis in this case)
        y = random.randrange(rows)                                                                                              # Variable that defines a built in python function that places specific elements at random places (food and the x axis in this case)
        if len(list(filter(lambda z:z.pos == (x,y) , positions))) > 0:                                                          # If statement that finds out if a position where the food is going to be placed is the same position as the snake figure, if so something happens
            continue                                                                                                            # If the if statement is true, then it runs again
        else:                                                                                                                   # If not then the loop stops
            break                                                                                                               # Stops the loop

    return (x, y)                                                                                                               # Returns x and y variables


def mainMessageWindow():
    '''Function that runs the main window when you die in the game, which includes menu's and choices''' 
    mainWin = Tk()                                                                                                              # Variable that defines the tkinter window as mainWin
    mainWin.title(f"You died.. Your score was: {len(s.body)}")                                                                  # Title on the window which is made in tkinter
    mainWin.geometry('400x200')                                                                                                 # Defines the size of the window which is made in tkinter
    message = "Do you want to save your score, exit, try again or show the leaderboard?"                                        # Variable that defines what the message will be
    Label(mainWin,text=message).pack()                                                                                          # A tekst element that is place over the buttons in the tkinter window
    Button(mainWin, text='Save', command=saveWindow).pack()                                                                     # Button that is made by tkinter which has the text Save and runs "saveWindow" function when it is pressed
    Button(mainWin, text='Close', command=exit).pack()                                                                          # Button that is made by tkinter which has the text Quit and runs "qut" function when it is pressed
    Button(mainWin, text='Try Again', command=mainWin.destroy).pack()                                                           # Button that is made by tkinter which has the text Try Again and runs "mainWin.destroy" function when it is pressed
    Button(mainWin, text='Show Leaderboard', command=showLeaderboard).pack()                                                    # Button that is made by tkinter which has the text Show Leaderboard and runs "showLeaderboard" function when it is pressed
    mainWin.mainloop()                                                                                                          # Calls back the tkinter window


def saveWindow():
    '''Function that creats the block that shows the input you are supposed to save to the database'''

    saveWin = Tk()                                                                                                              # Variable that defines tkinter window as saveWin
    saveWin.title('Save High Score')                                                                                            # Title on the window that is being made in tkinter
    saveWin.geometry('400x200')                                                                                                 # Defines the size of the window which is made in tkinter
    message = "Write your name!"                                                                                                # Variable that defines what the message will be
    Label(saveWin, text=message).pack()                                                                                         # A tekst element that is placed over the buttons in the tkinter window
    inputtxt = tk.Text(saveWin, height = 5, width = 20)                                                                         # Variable that defines and creates the text field in the tkinter window
    inputtxt.pack()                                                                                                             # Calls in the function pack() which makes everything visible on the screen


    def save():
        '''Function that runs the actual saving of information to the database'''
        SqlConnect()                                                                                                            # Function that is defined over, but is the connection to the database
        cursor = conn.cursor()                                                                                                  # Variable that defines the command, which is used later
        inputtxtget = inputtxt.get(1.0, "end-1c")                                                                               # This variable grabs the data you put in the text field which is then used later to be saved to the database
        query = f"INSERT INTO Attempts (Navn, Score, Dato) VALUES ('{inputtxtget}', {len(s.body)}, CURDATE())"                  # Variable that defines which information that shall be claimed or recieved to/from the database

        cursor.execute(query)                                                                                                   # Command that runs the variable "query"
        conn.commit()                                                                                                           # Command that saves and makes changes permanent in the database

        saveWin.destroy()                                                                                                       # Destroys the window after its done saving the data to the database

    Button(saveWin, text='Save', command=save).pack()                                                                           # Button that is made by tkinter which has the text save and runs the "save" function when its pressed
    
    
def showLeaderboard():
    '''Function that creates the block that shows the information for the leaderboard by connecting to the database'''
    leaderboardWin = tk.Tk()    
    leaderboardWin.title("Leaderboard")                                                                                         # Variable that defines the tkinter window as leaderboardWin
    leaderboardWin.geometry("400x200")                                                                                          # Defines the size on the window which is made in tkinter

    SqlConnect()                                                                                                                # Function that is defined over, but is the connection to the database
    cursor = conn.cursor()                                                                                                      # Variable that defines the command, which is used later
    query = "SELECT Navn, Score, DATE_FORMAT(Dato, '%d.%m.%Y') Dato FROM Attempts ORDER BY Score DESC LIMIT 0,5 "               # Variable that defines which information that shall be claimed or recieved to/from the database, 
                                                                                                                                # in addition puts it in order and limits how much shall be shown
    cursor.execute(query)                                                                                                       # Command that runs the variable "query"
    e = Label(leaderboardWin, width = 10, text = "Name",borderwidth = 2, relief = 'ridge', anchor = 'w') 
    e.grid(row=0, column=0)
    e = Label(leaderboardWin, width = 10, text = "Score",borderwidth = 2, relief = 'ridge', anchor = 'w') 
    e.grid(row=0, column=1)
    e = Label(leaderboardWin, width = 10, text = "Date",borderwidth = 2, relief = 'ridge', anchor = 'w') 
    e.grid(row=0, column=2)   
    i=1                                                                                                                         
    # Commands that creat a small table at the top of the tkinter box which places in name, placement, color and design

    for Attempts in cursor:                                                                                                     # For loop that checks for information in the table in the database
        for j in range(len(Attempts)):                                                                                          # For everytime it finds information, it places it in a table that is made in tkinter
            e = Label(leaderboardWin, width = 10, text = Attempts[j],borderwidth = 2, relief = 'ridge', anchor = 'w')           # Command that mkakes the table that is placed in tkinter box which decides, content, placement, color and design
            e.grid(row=i, column=j)                                                                                             # The tables definition
        i=i+1                                                                                                                   # After it goes through the first index, it pluses on 1 and does the same again

    close = Button(leaderboardWin, text='Close Window', command=leaderboardWin.destroy)
    close.grid(row = 6 , column = 1)


def main():
    '''Main function that runs in its entirety'''
    global s, snack                                                                                                             # Globalizes s and snake so that they can be used in different scenarios

    s = Snake((FGREEN), (10, 10))                                                                                               # Variable that defines "snake" as s and gets it from the "snake" class, afterwards gives it a start position and a color 
    snack = Cube(randomSnack(ROWS, s), color = (FYELLOW))                                                                       # Variable that defines the randomSnack function as snack and gets it from the "Cube" class, afterwards calls the randomSnack function and finally gives them a color and size
    win = pygame.display.set_mode((WIDTH, WIDTH))                                                                               # Variable that defines the size of the window in pygame and is being called as win
    flag = True                                                                                                                 # Sets flag while loop to true so that the loop runs
    clock = pygame.time.Clock()                                                                                                 # Variable that is defined as clock which decides how fast the program will run     

    while flag:                                                                                         
        '''While loop that runs the game'''
        pygame.time.delay(50)                                                                                                   # Command that slows the game by half a second so that the game runs at precisely 10 fps
        clock.tick(10)                                                                                                          # Command that decides the speed of the game, in this case it's 10 fps

        s.move()                                                                                                                # Calls in the move function that was defined in the snake class earlier in the program
        if s.body[0].pos == snack.pos:                                                                                          # A if statement that runs everytime the "snake eats food" in this case, its supposed to add a cube object on the snake figure and then spawn a new food
            s.addCube()                                                                                                         # Calls "addCube" function that was defined earlier in the program
            snack = Cube(randomSnack(ROWS, s), color = (FYELLOW))                                                               # Variable that defines the snack with size and color

        for x in range(len(s.body)):                                                                                            # For loop that checks all the snake figure position
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):                                                        # If statement that checks if the moving position of the snake is moving through, is the same position as the snake figure
                mainMessageWindow()                                                                                             # If yes, then this function runs
                s.reset((10, 10))                                                                                               # Afterwards then this function runs with a start position
                break                                                                                                           # And afterwards the for loop ends

        redrawWindow(win)                                                                                                       # Calls the redrawWindow function which was defined earlier in the program

main()                                                                                                                          # Calls back the main function

