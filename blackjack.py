import random
from tkinter import *
import sys
import webbrowser

class Card():
    amount = 52
    types = ["d","h","s","c"]
    numbers = range(1,14)
    
    def __init__(self,n,t):
        
        if n in Card.numbers and t in Card.types:
            self.__n = int(n)
            self.__t = str(t)
        else:
            return str("Invalid Input")

    @staticmethod
    def get_number(self):
        return self.__n
    @staticmethod
    def get_type(self):
        return self.__t
    @staticmethod
    def get_both(self):
        return str(self.__t)+str(self.__n)

    def __eq__(self,other):
        if self.__n == other.__n:
            return True 
        else:
            return False

    def __gt__(self,other):
        if self.__n > other.__n:
            return True
        else:
            return False

    def __lt__(self,other):
        if self.__n < other.__n:
            return True
        else:
            return False 

    def __str__(self):
        return str(self.__t)+str(self.__n)

    @staticmethod 
    def add(list_hand):
        added = []
        for x in list_hand:
            
            if x.__n >=10:
               added.append(10)
            else:
                if x.__n == 1:
                    pass
                else:
                    added.append(x.__n)
                    
            if x.__n == 1:
                if sum(added) + 11 == 21:
                    added.append(11)
                elif sum(added) + 11 < 21:
                    added.append(11)
                else:
                    added.append(1)
        return sum(added) 


class Card_Image:
    def __init__(self,canvas,x,y,name):
        self.img = images[name]
        self.id = canvas.create_image(x,y,image = self.img)
        self.canvas = canvas
        self.x = x
        self.y = y 
    def output(self,x,y):
        self.canvas.create_image(x,y,image = self.img)  
                



def give_hand(n,deck,hand):
    loop = True 
    while n > 0:
        random_digit = random.randint(0,len(deck)-1)
        hand.append(deck[random_digit])
        deck.pop(random_digit)
        n -= 1
    return hand 



def make_deck():
    deck = []
    loop = True
    while loop:
        for x in Card.types:
            for y in Card.numbers:
                card_of_deck = Card(y,x)
                deck.append(card_of_deck)
                if x == "c" and y == 13:
                    loop = False
    return deck


def draw_game(dealer_hand):
    if "game" in images:
        game = Card_Image(window,250,250,"game")
    else:
        pass 
    global deck_image,pic3,hidden_card,hit_button,reveal_button
    deck_image = Card_Image(window,100,180,"deck")
    deck_image.output(100,176)
    deck_image.output(100,172)
    window.create_text(100,125,text="DECK",fill="white")

    """user"""
    reveal_button.pack()
    reveal_button.place(x=95,y=400)
    hit_button.pack()
    hit_button.place(x=150,y=400)
    window.create_text(260,340,text=ENTRY.get(),fill="white")
    
    """ dealer """
    hidden_card = Card_Image(window,250,100,"back")
    n = Card.get_both(dealer_hand[1])
    pic3 = Card_Image(window,280,100,n)
    window.create_text(260,40,text="DEALER",fill="white")
    menu_button.place(x=10,y=10)
    pic_button.place(x=2000,y=4650)
    black_button.place(x=800,y=4650)
    red_button.place(x=1400,y=4650)
    green_button.place(x=1000,y=1000)


def hit(event=None):
    give_hand(1,deck,usr_hand)
    b = 30
    hidden_card.output(250,400)
    for x in range(1,len(usr_hand)):
        n = Card.get_both(usr_hand[x])
        a = Card_Image(window,250+b,400,n)
        list_of_cards.append(a)
        b+=30
    for x in list_of_cards:
        x.id


def exit_func(event=None):
    root.destroy()

def reveal(event=None):
    c = 0
    b = 0 
    window.delete("all")
    draw_game(dealer_hand)

    for x in range(len(dealer_hand)):
        n = Card.get_both(dealer_hand[x])
        a = Card_Image(window,250+c,100,n)
        c+=30
    for x in range(len(usr_hand)):
        n = Card.get_both(usr_hand[x])
        a = Card_Image(window,250+b,400,n)
        b+=30

    a = Card.add(usr_hand)
    d = Card.add(dealer_hand)

    if d < a < 22:
        window.create_text(250,250,text="YOU WON",fill="green",font=("Arial",16))
    elif a > 21:
        window.create_text(250,250,text="BUST",fill="red",font=("Arial",16))
    elif d > a:
        if d > 21 and a <= 21:
            window.create_text(250,250,text="YOU WON",fill="red",font=("Arial",16))
        else:
            window.create_text(250,250,text="YOU LOST",fill="red",font=("Arial",16))
    elif d == a:
        window.create_text(250,250,text="DRAW",fill="blue",font=("Arial",16))
    

    usr_total = "Total:"+str(a)
    window.create_text(255,460,text=usr_total, fill="white")
    dealer_total = "Total:"+str(d)
    window.create_text(255,160,text=dealer_total,fill="white")
    window.create_text(255,270,text="RESTART?",fill="white",font=(None,14))
    exit_button.pack()
    exit_button.place(x=252,y=280)
    start_button.pack()
    start_button.place(x=215,y=280)
    reveal_button.place(x=600,y=700)
    hit_button.place(x=600,y=700)
    

def new_game(event=None):
    window.delete("all")
    menu_button.place(x=10,y=10)
    if "game" in images:
        game = Card_Image(window,250,250,"game")
    else:
        pass 
    start_button.place(x=700,y=700)
    exit_button.place(x=600,y=700)
    deck = make_deck()
    global dealer_hand
    dealer_hand = []
    dealer_hand = give_hand(2,deck,dealer_hand)
    draw_game(dealer_hand)
    list_of_cards = []
    global usr_hand
    usr_hand = []
    window.pack()
    window.mainloop()
    
    
def callback(event=None):
    e.place(x=1000,y=1000)
    usr_entry.place(x=1000,y=1000)
    window.delete("all")
    new_game(dealer_hand)

def link_button(event=None):
    link = "http://entertainment.howstuffworks.com/how-to-play-blackjack.htm"
    return webbrowser.open(link)

def menu(event=None):
    window.delete("all")
    welcome = Card_Image(window,250,250,"welcome")
    window.create_window(420,440,window=e,tags="entry")
    usr_entry.pack()
    usr_entry.place(x=400,y=460)
    window.create_text(110,420,text="BLACKJACK",fill="white",font=("Arial",22))
    window.create_text(325,440,text="Name:",fill="white")
    window.create_text(420,418,text="WELCOME",fill="white",font=("Arial",13))
    window.create_text(110,450,text="Press R for Rules",fill="orange",font=("Arial",14))
##    window.create_text(423,80,text="Change Background",fill="white",font=("Arial",12))
    start_button.place(x=1000,y=1000)
    exit_button.place(x=1000,y=1000)
    hit_button.place(x=1000,y=1000)
    reveal_button.place(x=1000,y=1000)
    menu_button.place(x=1000,y=1000)
    pic_button.place(x=20,y=465)
    black_button.place(x=80,y=465)
    red_button.place(x=140,y=465)
    green_button.place(x=200,y=465)

def change_bg(event=None):
    if bg_option.get() == "game":
        images["game"] = PhotoImage(file = "cards/game.gif")
        pass
    else:
        if "game" in images:
            del images["game"]
        window.configure(bg=bg_option.get())


#MAIN VARIABLES#
root = Tk()
window = Canvas(root,width=500,height=500,bg="dark green")
hit_button = Button(root,text="HIT", fg = "red",command=hit)
reveal_button = Button(root,text="REVEAL",fg="blue",command=reveal)
exit_button = Button(root,text="EXIT",fg="red",command=exit_func)
start_button = Button(root,text="YES",fg="blue",command=new_game)
menu_button = Button(root,text="Menu",fg="purple",command=menu)
root.bind("<Shift-Key-R>",link_button)
root.bind("<Escape>",exit_func)
usr_entry = Button(window,text="Enter",fg="blue",command=callback)

bg_option = StringVar(value="fadd")
green_button = Radiobutton(window,text="Green",command=change_bg,variable=bg_option,value="dark green",width=5,bg="dark red",fg="black")
black_button = Radiobutton(window,text="Black",command=change_bg,variable=bg_option,value="black",width=5,bg="dark red",fg="black")
red_button = Radiobutton(window,text="Red",command=change_bg,variable=bg_option,value="dark red",width=5,bg="dark red",fg="black")
pic_button = Radiobutton(window,text="Picture",command=change_bg,variable=bg_option,value="game",width=5,bg="dark red",fg="black")


ENTRY = StringVar()
e = Entry(window,textvariable=ENTRY)
e.bind("<Return>",callback)
deck = make_deck()
list_of_cards = []
usr_hand = []
dealer_hand = []
dealer_hand = give_hand(2,deck,dealer_hand)
""" dictionary of images """ 
images = {}
images["back"] = PhotoImage(file = "cards/back.gif")
images["deck"] = PhotoImage(file = "cards/deck.gif")
images["welcome"] = PhotoImage(file="cards/welcome.gif")

for suit in "dhcs":
    for i in range(1,14):
        name = suit+str(i)
        images[name] = PhotoImage(file = "cards/%s.gif"%name)


#MAIN PROGRAM
menu()
window.pack()
window.mainloop()



