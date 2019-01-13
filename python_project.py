from Tkinter import*
import Tkinter as tk
from tkMessageBox import*
import pygame, random, sys
from pygame.locals import *
import sqlite3
import time;
import webbrowser
import splash
splash.splashscreen()



root=Tk()
root.title("Online_Shopping_Mall")
root.configure(background="gainsboro")
Label(root, text="IP MALL\n Durgakund Rd, Bhelupur Varanasi, 221002\n Hours: 9AM-10PM\n Phone: 0542-2277950", relief="ridge", font="times 20", fg="ivory3", bg="crimson").grid(row=0, column=2)
Label(root, text="pantaloons", bg="aquamarine3", fg="white", font="times 10 bold", relief="ridge", height=8, width=13).grid(row=0, column=3)
Label(root, text="Domino's\nPh: 2221758-63", bg="blue", fg="white", font="tiems 10 bold", relief="ridge").grid(row=1, column=3)
Label(root, text="NO PARKING\tNO PARKING\tNO PARKING\tNO PARKING\tNO PARKING", fg="red", bg="yellow2", height=1, width=70, font="times 10").grid(row=2, column=2)
Label(root, height=6, width=20, bg="purple4", relief="ridge").grid(row=0, column=0)
Label(root, height=4, width=16, bg="red", relief="ridge").grid(row=0, column=0)
Label(root, height=6, width=12, bg="purple4", relief="ridge").grid(row=0, column=0)
Label(root, height=4, width=8, bg="red", relief="ridge").grid(row=0, column=0)
Label(root, height=4, width=4, bg="purple4", relief="ridge").grid(row=0, column=0)
Label(root, height=4, width=2, bg="red", relief="ridge").grid(row=0, column=0)
Label(root, text="BIKANERVALA", fg="white", bg="yellow2", font="times 15 bold", relief="ridge").grid(row=0, column=0)

def clock():
    t=time.strftime("%y-%m-%d\n %H:%M:%S", time.localtime())
    if t!="":
        Label(root, text=t, font="times 8 bold", width=13, bg="gainsboro", relief="ridge").grid(row=2, column=3)
    root.after(100, clock)
clock()



def fun1():
    root.destroy()

def fun():
    root=Tk()
    root.title("Main_storey")
    root.configure(bg="antiquewhite1")
    Label(root, text="MAIN STOREY", font="times 20", bg="antiquewhite1").grid(row=0, column=1)
    Label(root, text="Get up to 20% discount on every sale and chance to win a trip to Madagascar", font="times 10", bg="antiquewhite1").grid(row=1, column=0)
    Label(root, text="BIG! BIG! SALE", font="times 25", fg="white", bg="red").grid(row=0, column=0)

    Label(root, text="paytm", font="times 20", bg="antiquewhite1", fg="blue").grid(row=0, column=2)

    def fun1():
        root.destroy()
    def fun2():
        root=Tk()
        root.title("Restro")
        root.configure(bg="aliceblue")
        Label(root, text="Restaurant :\tRating-(4.1*)", bg="aliceblue").grid(row=1, column=0)

        def domino():
            root=Tk()
            root.title("Domino")
            root.configure(background="blue")
            Label(root, text="Domino's : The Pizza divilery expert", font="times 30", relief="ridge", fg="white", bg="blue").grid(row=0, column=0, columnspan=6)
            Label(root, text="Item", font="times 10 bold", bg="blue").grid(row=1, column=0)
            Label(root, text="Price per Plate", font="times 10 bold", bg="blue").grid(row=1, column=1)
            Label(root, text="Quantity", font="times 10 bold", bg="blue").grid(row=1, column=2)

            Label(root, text="Item", font="times 10 bold", bg="blue").grid(row=1, column=3)
            Label(root, text="Price per Plate", font="times 10 bold", bg="blue").grid(row=1, column=4)
            Label(root, text="Quantity", font="times 10 bold", bg="blue").grid(row=1, column=5)

            Label(root, text="Veg Pizza", font="times 15", bg="blue", fg="white").grid(row=2, column=0)
            Label(root, text="₹ 95/-", bg="blue").grid(row=2, column=1)
            e1=Entry(root,width=10)
            e1.grid(row=2, column=2)
            e1.insert(0,'0')

            Label(root, text="Margherita", font="times 15", bg="blue", fg="white").grid(row=3, column=0)
            Label(root, text="₹ 375/-", bg="blue").grid(row=3, column=1)
            e2=Entry(root,width=10)
            e2.grid(row=3, column=2)
            e2.insert(0,'0')

            Label(root, text="Farm House", font="times 15", bg="blue", fg="white").grid(row=4, column=0)
            Label(root, text="₹ 155/-", bg="blue").grid(row=4, column=1)
            e3=Entry(root,width=10)
            e3.grid(row=4, column=2)
            e3.insert(0,'0')

            Label(root, text="Peepy-Paneet", font="times 15", bg="blue", fg="white").grid(row=5, column=0)
            Label(root, text="₹ 199/-", bg="blue").grid(row=5, column=1)
            e4=Entry(root,width=10)
            e4.grid(row=5, column=2)
            e4.insert(0,'0')

            Label(root, text="Mexican-Green-Wave", font="times 15", bg="blue", fg="white").grid(row=6, column=0)
            Label(root, text="₹ 255/-", bg="blue").grid(row=6, column=1)
            e5=Entry(root,width=10)
            e5.grid(row=6, column=2)
            e5.insert(0,'0')

            Label(root, text="Cheese-n-Corn", font="times 15", bg="blue", fg="white").grid(row=2, column=3)
            Label(root, text="₹ 375/-", bg="blue").grid(row=2, column=4)
            e6=Entry(root,width=10)
            e6.grid(row=2, column=5)
            e6.insert(0,'0')

            Label(root, text="Deluxe-Veggie", font="times 15", bg="blue", fg="white").grid(row=3, column=3)
            Label(root, text="₹ 415/-", bg="blue").grid(row=3, column=4)
            e7=Entry(root,width=10)
            e7.grid(row=3, column=5)
            e7.insert(0,'0')

            Label(root, text="Veggie-Paradise", font="times 15", bg="blue", fg="white").grid(row=4, column=3)
            Label(root, text="₹ 225/-", bg="blue").grid(row=4, column=4)
            e8=Entry(root,width=10)
            e8.grid(row=4, column=5)
            e8.insert(0,'0')

            Label(root, text="Medium-Sized", font="times 15", bg="blue", fg="white").grid(row=5, column=3)
            Label(root, text="₹ 195/-", bg="blue").grid(row=5, column=4)
            e9=Entry(root,width=10)
            e9.grid(row=5, column=5)
            e9.insert(0,'0')

            Label(root, text="Small-Cheese", font="times 15", bg="blue", fg="white").grid(row=6, column=3)
            Label(root, text="₹ 105/-", bg="blue").grid(row=6, column=4)
            e10=Entry(root,width=10)
            e10.grid(row=6, column=5)
            e10.insert(0,'0')

            Label(root, text="Pay :", fg="white", bg="blue").grid(row=8, column=6)
            e11=Entry(root, width=10)
            e11.grid(row=8, column=7)
            Label(root, text="Bill+GST", fg="white", bg="blue").grid(row=9, column=6)
            e12=Entry(root, width=10)
            e12.grid(row=9, column=7)
            
            def bill_pay():
                val = int(e1.get())*95+int(e2.get())*375+int(e3.get())*155+int(e4.get())*199+int(e5.get())*225+int(e6.get())*375+int(e7.get())*415+int(e8.get())*225++int(e9.get())*195++int(e10.get())*105
                val = str(val)
                e11.insert(0,val)
                val=int(val)
                val = val+val*5/100.0
                e12.insert(0,val)

                            
            def clear():
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e7.delete(0, END)
                e8.delete(0, END)
                e9.delete(0, END)
                e10.delete(0, END)
                e11.delete(0, END)
                e12.delete(0, END)
                
            Button(root, text="Clear", bg="gray", command=clear).grid(row=7, column=0)
            Button(root, text="Place & Payment", bg="gray", command=bill_pay).grid(row=7, column=1)
            
            def Leave():
                root.destroy()
            Button(root, text="Leave", bg="yellow2", fg="red", width=8, command=Leave).grid(row=7, column=5)

            
        Button(root, text="Domino's\n The Pizza delivery Experts", bg="blue", fg="white", font="times 10 bold", command=domino).grid(row=2, column=0)
        Label(root, text="--ALL NEW : DOMINO'S  OREDER NOW--", fg="blue", bg="aliceblue", font="times 10").grid(row=2, column=1)
        Button(root, text="McDonald's\n i'm lovin' it", bg="yellow4", fg="yellow", font="times 10 bold").grid(row=3, column=1)
        Label(root, text="Place your Order Here : Happy Meal\nCall us for Dilivery ☎: 66000666", fg="orange", bg="aliceblue").grid(row=3, column=0)
        Button(root, text="Bikanervala\n india sweets", bg="purple4", fg="white", font="times 10 bold").grid(row=4, column=3)
        Label(root, text="A tradition of taste!! since 1950", fg="white", bg="springgreen2").grid(row=4, column=1)
        Label(root, text="Need Help? cll us at✆ +91 9871590661", fg="white", bg="springgreen2").grid(row=4, column=0)
        Button(root, text="kfc ®\n it's finger lickin' good", bg="red3", fg="white", font="times 10 bold").grid(row=5, column=4)
        Label(root, text="ORDER QUICK WITH ONE CLICK BUTTON\n KFC button", fg="crimson", bg="aliceblue").grid(row=5, column=1)
        

           
        def out():
            root.destroy()
        Button(root, text="Leave", bg="yellow2", fg="red", width=15, command=out).grid(row=8, column=0)

        
    Button(root, text="Grond_floor", bg="gray", font="times 10 bold", command=fun2, width=9, height=8, bd=3, relief="ridge").grid(row=2, column=0)
    Label(root, text="Restaurant Section", bg="antiquewhite1", font="times 10 bold").grid(row=3, column=0)

    def move_in():
        root=Tk()
        root.configure(background="thistle1")
        root.title("Clothings")
        Label(root, text="Stores :", bg="thistle1").grid(row=0, column=0)
        def pantaloons():
            Label(root, text="welcom to pantaloons\n in❤with fashion", font="times 10", bg="thistle1").grid(row=2, column=1)
            
            def women():
                Label(root, text="Ethnic Wear", font="times 10 bold", bg="thistle1").grid(row=4, column=0)
                Label(root, text="Casual Wear", font="times 10 bold", bg="thistle1").grid(row=4, column=1)
                Label(root, text="Formal Wear", font="times 10 bold", bg="thistle1").grid(row=4, column=2)
                Label(root, text="Akkriti", bg="thistle1").grid(row=5, column=0)
                Label(root, text="Rangmanch", bg="thistle1").grid(row=6, column=0)
                Label(root, text="Trishaa", bg="thistle1").grid(row=7, column=0)
                Label(root, text="Jamini", bg="thistle1").grid(row=8, column=0)
                Label(root, text="Izabel London", bg="thistle1").grid(row=5, column=1)
                Label(root, text="Candie's, New York", bg="thistle1").grid(row=6, column=1)
                Label(root, text="SF Jeans", bg="thistle1").grid(row=7, column=1)
                Label(root, text="Honey", bg="thistle1").grid(row=8, column=1)
                Label(root, text="Bare Denim", bg="thistle1").grid(row=8, column=1)
                Label(root, text="Annabelle", bg="thistle1").grid(row=5, column=2)
                Label(root, text="Plus Size Fashion", font="times 10 bold", bg="thistle1").grid(row=6, column=2)
                Label(root, text="Alto Moda", bg="thistle1").grid(row=7, column=2)
                Label(root, text="Ajile", bg="thistle1").grid(row=8, column=2)
            Button(root, text="WOMEN'S COLLECTION", bg="gray", fg="aquamarine1", command=women).grid(row=3, column=0)

            
            
            def men():
                Label(root, text="Formal Wear", font="times 10 bold", bg="thistle1").grid(row=4, column=0)
                Label(root, text="Casual Wear", font="times 10 bold", bg="thistle1").grid(row=4, column=1)
                Label(root, text="Active Wear", font="times 10 bold", bg="thistle1").grid(row=4, column=2)
                Label(root, text="Lombard", bg="thistle1").grid(row=5, column=0)
                Label(root, text="Evening Wear", font="times 10 bold", bg="thistle1").grid(row=6, column=0)
                Label(root, text="F Factor", bg="thistle1").grid(row=7, column=0)
                Label(root, text="Plus Size Fashion", font="times 10 bold", bg="thistle1").grid(row=8, column=0)
                Label(root, text="Alto Monda", bg="thistle1").grid(row=9, column=0)
                Label(root, text="Byford", bg="thistle1").grid(row=5, column=1)
                Label(root, text="Bare Denim", bg="thistle1").grid(row=6, column=1)
                Label(root, text="Bare Leisure", bg="thistle1").grid(row=7, column=1)
                Label(root, text="Rig", bg="thistle1").grid(row=8, column=1)
                Label(root, text="JM Sports", bg="thistle1").grid(row=8, column=1)
                Label(root, text="Ajile", bg="thistle1").grid(row=5, column=2)
                Label(root, text="Ethnic Wear", font="times 10 bold", bg="thistle1").grid(row=6, column=2)
                Label(root, text="Indus Route", bg="thistle1").grid(row=7, column=2)
                
                
            Button(root, text="MEN'S COLLECTION", bg="gray", fg="aquamarine1", command=men).grid(row=3, column=1)

            def kid():
                Label(root, text="Kids Casual Wear", font="times 10 bold", bg="thistle1").grid(row=4, column=0)
                Label(root, text="Chirpie Pie(0-2 yrs)", bg="thistle1").grid(row=5, column=0)
                Label(root, text="Chalk(2-7 yrs)", bg="thistle1").grid(row=6, column=0)
                Label(root, text="Poppers(2-7 yrs)", bg="thistle1").grid(row=7, column=0)
                Label(root, text="Bare Kids(2-7 yrs)", bg="thistle1").grid(row=8, column=0)
                Label(root, text="Kids Ethnic Wear", font="times 10 bold", bg="thistle1").grid(row=4, column=1)
                Label(root, text="Akkriti(7-12 yrs)", bg="thistle1").grid(row=5, column=1)
            Button(root, text="KIDS COLLECTION", bg="gray", fg="aquamarine1", command=kid).grid(row=3, column=2)
        Button(root, text="pantaloons", bg="aquamarine3", fg="white", font="times 10", command=pantaloons).grid(row=1, column=1)

        def levi():
            Label(root, text="TOGETHERNESS IS IN OUR JEANS", font="times 12 bold", bg="thistle1").grid(row=4, column=2)
            Label(root, text="GET READY FOR GOOD TIMES IN ALL YOUR FAVORITES STYLES", font="times 7", bg="thistle1").grid(row=5, column=2);
            var=StringVar(root)
            var.set("SHOP MEN")
            def grab_and_assign(event):
                chosen_option=var.get()
                label_chosen_variable=Label(root, text=chosen_option)
                
            drop_menu=OptionMenu(root, var, "Levi's® Commuter™ Trucker Jacket with Jacquard™ by Google", "Levi's® x Rolling Stone Graphic Tee", "Levi's® x Rolling Stone Graphic Tee" , "514™ Straight Fit Jeans", "Levi's®  505™ Regular Fit Workwear", "Levi's® 505™ Regular Fit Workwear Cargo Pants", "Levi's® 545 Athletic Fit Workwear Utility Jeans", "Classic One Pocket Shirt", "511™ Slim Fit Brushed 5-Pocket Pant", command=grab_and_assign).grid(row=6, column=2)
    
            var1=StringVar(root)
            var1.set("SHOP WOMEN")
            def grab_and_assign1(event):
                chosen_option=var1.get()
                label_chosen_variable=Label(root, text=chosen_option)
            drop_menu=OptionMenu(root, var1, "Levi's® Commuter™ Trucker Jacket with Jacquard™ by Google", "Ex-Boyfriend Trucker Jacket", "Lurex Sweater", "710 Warm Super Skinny Jeans", "Wool Boyfriend Sherpa Trucker", "Levi's® x Rolling Stone 501® Festival Short", "501® Shorts", "Levi's® x Rolling Stone Graphic Tee", "Levi's® X Rolling Stone Authentic Graphic Tee", "Relaxed Crewneck Sweatshirt",   command=grab_and_assign).grid(row=7, column=2)
        Button(root, text="Levi's ®", bg="red2", fg="white", font="times 10", command=levi).grid(row=1, column=2)

        def lara():
            Label(root, text="FOLLOW @LARAFASHIONUSA ON INSTRAGRAM", font="times 10 bold", bg="thistle1").grid(row=4, column=3)
            def larafashionusa():
                def window_shop():
                    def shop():
                        Label(root, text="All product", bg="thistle1").grid(row=10, column=2)
                        Label(root, text="Tops", bg="thistle1").grid(row=11, column=2)
                        Label(root, text="Bottoms", bg="thistle1").grid(row=12, column=2)
                        Label(root, text="Dresses", bg="thistle1").grid(row=13, column=2)
                        Label(root, text="Out wear", bg="thistle1").grid(row=14, column=2)
                        Label(root, text="Plus size", bg="thistle1").grid(row=15, column=2)
                    Button(root, text="SHOP", font="times 10 bold", command=shop, bg="thistle1").grid(row=9, column=2)
                    
                    def special():
                        Label(root, text="Sale!", bg="thistle1").grid(row=10, column=3)
                        Label(root, text="Last call", bg="thistle1").grid(row=11, column=3)
                    Button(root, text="SPECIAL", font="times 10 bold", command=special, bg="thistle1").grid(row=9, column=3)
                    def season():
                        Label(root, text="Fall winter 2017", bg="thistle1").grid(row=10, column=4)
                        Label(root, text="Spring summer 2017", bg="thistle1").grid(row=11, column=4)
                        Label(root, text="Fall winter 2016", bg="thistle1").grid(row=12, column=4)
                    Button(root, text="SEASON", font="times 10 bold", command=season, bg="thistle1").grid(row=9, column=4)
                    
                Button(root, text="Window Shopping", font="ALGERIAN 10", command=window_shop, bg="thistle1").grid(row=8, column=3)
                    
                
            Button(root, text="2017\n 1ST ANNUAL\n CLEARANCE\nSALE EVENT", height=8, width=15, relief="ridge", command=larafashionusa, bg="thistle1").grid(row=5, column=3)
            Label(root, text="SHOP NOW", bg="red", fg="white").grid(row=6, column=3)
            Label(root, text="LARA FASHION", bg="thistle1").grid(row=7, column=3)
        Button(root, text="LARA", bg="brown3", font="times 10", command=lara).grid(row=1, column=3)

        def john_players():
            var2=StringVar(root)
            var2.set("Formals")
            def grab_and_assign2(event):
                chosen_option=var2.get()
                label_chosen_variable=Label(root, text=chosen_option)
            drop_menu=OptionMenu(root, var2, "Augment your style quotient with this light color polka dots shirt by John Players that is designed with absolute fineness., ", "A slim fit classic shirt for that important meeting or an interview , a must have for your wardrobe., ", "Go bold,this slim fit 100% cotton shirt with this unique FASHION formal shirt from John Players.", command=grab_and_assign2).grid(row=2, column=4)

            var3=StringVar(root)
            var3.set("Casual wear")
            def grab_and_assign3(event):
                chosen_option=var3.get()
                label_chosen_variable=Label(root, text=chosen_option)
            drop_menu=OptionMenu(root, var3, "Stay a fashionista of the highest order, when you wear this slim fit printed shirt with a casual trouser.", "Immerse urself in solids with this shirt paired with slim fit trouser,a must have for this autumn winter,", "Stay a fashionista of the highest order, when you wear this slim fit sweater with a casual trouser. , ", command=grab_and_assign3).grid(row=3, column=4)

            var4=StringVar(root)
            var4.set("John Jeans")
            def grab_and_assign4(event):
                chosen_option=var4.get()
                label_chosen_variable=Label(root, text=chosen_option)
            drop_menu=OptionMenu(root, var4, "Floral printed shirt this winter to enhance your style quotient when paired with slim fit trouser/jeans,", "Fun, playful, quirky - Collection of graphic tees from John Players Jeans . A natural addition to your tee collection.,", command=grab_and_assign4).grid(row=4, column=4)
        Button(root, text="JOHN PLAYERS", bg="blue", fg="red2", font="times 10", command=john_players).grid(row=1, column=4)
        Button(root, text="Buffalo", font="times 10", bg="white").grid(row=1, column=5)

        def Leave():
            root.destroy()
        Button(root, text="Leave", bg="yellow2", fg="red", command=Leave, width=6).grid(row=5, column=5)
        def back():
            root.destroy()
            move_in()
        Button(root, text="back", command=back, font="times 10 bold", bg="aquamarine3", height=3, width=6).grid(row=4, column=5)
             
    Button(root, text="First_floor", bg="gray", font="times 10 bold", command=move_in, width=9, height=8, bd=3, relief="ridge").grid(row=2, column=1)
    Label(root, text="Clothing", bg="antiquewhite1", font="times 10 bold").grid(row=3, column=1)
    def second_floor():
        root=Tk()
        root.configure(background="orchid1")
        Label(root, text="Games & Stuffs\n  ❤", font="times 20", bg="orchid1", bd=3).grid(row=1, column=0, columnspan=4)
        
        def snake():
            def collide(x1, x2, y1, y2, w1, w2, h1, h2):
                if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:return True
                else:return False
            def die(screen, score):
                f=pygame.font.SysFont('Arial', 30);t=f.render('Your score was: '+str(score), True, (0, 0, 0));screen.blit(t, (10, 270));pygame.display.update();pygame.time.wait(2000);sys.exit(0)
            xs = [290, 290, 290, 290, 290];ys = [290, 270, 250, 230, 210];dirs = 0;score = 0;applepos = (random.randint(0, 590), random.randint(0, 590));pygame.init();s=pygame.display.set_mode((600, 600));pygame.display.set_caption('Snake');appleimage = pygame.Surface((10, 10));appleimage.fill((0, 255, 0));img = pygame.Surface((20, 20));img.fill((255, 0, 0));f = pygame.font.SysFont('Arial', 20);clock = pygame.time.Clock()
            while True:
                clock.tick(10)
                for e in pygame.event.get():
                    if e.type == QUIT:
                            sys.exit(0)
                    elif e.type == KEYDOWN:
                            if e.key == K_UP and dirs != 0:dirs = 2
                            elif e.key == K_DOWN and dirs != 2:dirs = 0
                            elif e.key == K_LEFT and dirs != 1:dirs = 3
                            elif e.key == K_RIGHT and dirs != 3:dirs = 1
                i = len(xs)-1
                while i >= 2:
                    if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):die(s, score)
                    i-= 1
                if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):score+=1;xs.append(700);ys.append(700);applepos=(random.randint(0,590),random.randint(0,590))
                if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580: die(s, score)
                i = len(xs)-1
                while i >= 1:
                    xs[i] = xs[i-1];ys[i] = ys[i-1];i -= 1
                if dirs==0:ys[0] += 20
                elif dirs==1:xs[0] += 20
                elif dirs==2:ys[0] -= 20
                elif dirs==3:xs[0] -= 20	
                s.fill((255, 255, 255))	
                for i in range(0, len(xs)):
                    s.blit(img, (xs[i], ys[i]))
                s.blit(appleimage, applepos);t=f.render(str(score), True, (0, 0, 0));s.blit(t, (10, 10));pygame.display.update()
  
        Button(root, text="Snake_Game", font="times 15", bg="black", fg="white", command=snake).grid(row=2, column=0)

        
        def tic_tac_toe():
            def print_board(board):

                print "The board look like this: \n"

                for i in range(3):
                    print " ",
                    for j in range(3):
                            if board[i*3+j] == 1:
                                    print 'X',
                            elif board[i*3+j] == 0:
                                    print 'O',	
                            elif board[i*3+j] != -1:
                                    print board[i*3+j]-1,
                            else:
                                    print ' ',
			
                            if j != 2:
                                    print " | ",
                    print
		
                    if i != 2:
                            print "-----------------"
                    else: 
                            print 
			
            def print_instruction():
                    print "Please use the following cell numbers to make your move"
                    print_board([2,3,4,5,6,7,8,9,10])


            def get_input(turn):

                valid = False
                while not valid:
                    try:
                            user = raw_input("Where would you like to place " + turn + " (1-9)? ")
                            user = int(user)
                            if user >= 1 and user <= 9:
                                    return user-1
                            else:
                                    print "That is not a valid move! Please try again.\n"
                                    print_instruction()
                    except Exception as e:
                            print user + " is not a valid move! Please try again.\n"
		
            def check_win(board):
                    win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
                    for each in win_cond:
                            try:
                                    if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
                                            return board[each[0]-1]
                            except:
                                    pass
                    return -1

            def quit_game(board,msg):
                    print_board(board)
                    print msg
                    quit()

            def main():
	
	# setup game
	# alternate turns
	# check if win or end
	# quit and show the board
	
                    print_instruction()

                    board = []
                    for i in range(9):
                            board.append(-1)

                    win = False
                    move = 0
                    while not win:

                    # print board
                            print_board(board)
                            print "Turn number " + str(move+1)
                            if move % 2 == 0:
                                    turn = 'X'
                            else:
                                    turn = 'O'

		# get user input
                            user = get_input(turn)
                            while board[user] != -1:
                                    print "Invalid move! Cell already taken. Please try again.\n"
                                    user = get_input(turn)
                            board[user] = 1 if turn == 'X' else 0

		# advance move and check for end game
                            move += 1
                            if move > 4:
                                    winner = check_win(board)
                                    if winner != -1:
                                            out = "The winner is " 
                                            out += "X" if winner == 1 else "O" 
                                            out += " :)"
                                            quit_game(board,out)
                                    elif move == 9:
                                            quit_game(board,"No winner :(")

            if __name__ == "__main__":
                    main()
	

        Button(root, text="Tic Tac Toe", font="times 15", fg="black", bg="white", command=tic_tac_toe).grid(row=2, column=1)
        
    Button(root, text="Second_floor", bg="gray",font="times 10 bold", width=9, height=8, bd=3, relief="ridge", command=second_floor).grid(row=2, column=2)
    Label(root, text="ball pool, hooka parlour and gaming zone", bg="antiquewhite1", font="times 10 bold").grid(row=3, column=2)
    def fun3():
        root=Tk()
        root.configure(background="aquamarine3")
        Label(root, text="PVR\ncinemas ®", bg="black", fg="yellow").grid(row=0, column=0)

        def duvvada_jagannadham():
            webbrowser.open("https://www.youtube.com/watch?v=zMxIW7uwDGg")
        var=StringVar(root)
        var.set("Book Ticket")
        option=OptionMenu(root, var, "9:00 am to 11:45pm", "12:15pm to 3:00pm", "3:00pm to 5:45pm")
        option.grid(row=2, column=0)
        Label(root, text="Duvvada Jagannadham", bg="aquamarine3").grid(row=1, column=0)
        Button(root, text="Move_in", bg="aquamarine3", command=duvvada_jagannadham).grid(row=3, column=0)

        def aakash_vani():
            webbrowser.open("https//https://www.youtube.com/watch?v=CRvoJEqrYTY")
        var=StringVar(root)
        var.set("Book Ticket")
        option=OptionMenu(root, var, "9:00 am to 11:45pm", "12:15pm to 3:00pm", "3:00pm to 5:45pm")
        option.grid(row=2, column=1)
        Label(root, text="Aakash Vani", bg="aquamarine3").grid(row=1, column=1)
        Button(root, text="Move_in", font="times 10", bg="aquamarine3", command=aakash_vani).grid(row=3, column=1)
        
        def escape_plan():
            webbrowser.open("https://www.youtube.com/watch?v=yp9LGBoDpf8&t=253s")
        var=StringVar(root)
        var.set("Book Ticket")
        option=OptionMenu(root, var, "9:00 am to 11:45pm", "12:15pm to 3:00pm", "3:00pm to 5:45pm")
        option.grid(row=2, column=2)
        Label(root, text="Escape Plan", bg="aquamarine3").grid(row=1, column=2)
        Button(root, text="Move_in", font="times 10", bg="aquamarine3").grid(row=3, column=2)

        
        def move_out():
            root.destroy()
        Button(root, text="Move_out", command=move_out, bg="DarkOrchid1").grid(row=0, column=4)
        
    Button(root, text="BOX OFFICE", bg="skyblue", height=6, width=8, command=fun3).grid(row=2, column=5)
    Button(root, text="EXIT", bg="red", width=8, command=fun1).grid(row=3, column=5)
    root.mainloop()

    
Button(root, text="ENTER", bg="spring green2", font="times 10 bold", command=fun, height=1, width=16).grid(row=1, column=0)
Button(root, text="EXIT", bg="red", font="times 10 bold", command=fun1, height=1, width=12).grid(row=2, column=0)
root.mainloop()


