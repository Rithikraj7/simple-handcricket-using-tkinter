import random
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import simpledialog

window = tk.Tk()
name_var = tk.StringVar()
language_var = tk.StringVar()

window.geometry("1200x800")
bg = ImageTk.PhotoImage(Image.open("D:/numberplate/QT-Cricket.jpg"))
label17 = Label(window, image=bg)
label17.place(x=0, y=0)
label8 = Label(window, text="Hand cricket",font="times 38 bold")
label8.place(x=600, y=50, anchor="center")


img1=ImageTk.PhotoImage(Image.open("D:/hands/1.jpeg"))
img2=ImageTk.PhotoImage(Image.open("D:/hands/2.jpeg"))
img3=ImageTk.PhotoImage(Image.open("D:/hands/3.jpeg"))
img4=ImageTk.PhotoImage(Image.open("D:/hands/4.jpeg"))
img5=ImageTk.PhotoImage(Image.open("D:/hands/5.jpeg"))
img6=ImageTk.PhotoImage(Image.open("D:/hands/6.jpeg"))
img7=ImageTk.PhotoImage(Image.open("D:/hands/7.jpeg"))
img8=ImageTk.PhotoImage(Image.open("D:/hands/8.jpeg"))
img9=ImageTk.PhotoImage(Image.open("D:/hands/9.jpeg"))
img10=ImageTk.PhotoImage(Image.open("D:/hands/10.jpeg"))

def enterIMG():
    image_list = random.choice([img1,img2,img3,img4,img5,img6,img7,img8,img9,img10])
    image_list1 = random.choice([img1,img2,img3,img4,img5,img6,img7,img8,img9,img10])
    my_label1= Label(image=image_list)
    my_label1.place(x=100,y=200)
    my_label2= Label(image=image_list1)
    my_label2.place(x=800,y=200)

language_var = tk.IntVar()
def cointoss():
    return random.choice(["head", "tail"])
def function():
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chances_1 = 6
    no_of_chances_1 = 0
    your_runs = 0
    label89 = Label(window, text="your batting", font="times 28 bold")
    label89.place(x=600, y=600, anchor="center")

    while no_of_chances_1 < chances_1:
        runs = simpledialog.askinteger('input box', 'enter the runs')
        img101 = ImageTk.PhotoImage(Image.open("D:/hands/"+str(runs)+".jpeg"))
        my_label1 = Label(image=img101)
        my_label1.place(x=100, y=200)
        comp_bowl = random.choice(lst1)
        img10 = ImageTk.PhotoImage(Image.open("D:/hands/" + str(comp_bowl) + ".jpeg"))
        my_label14 = Label(image=img10)
        my_label14.place(x=800, y=200)

        if runs == comp_bowl:
            hello=Label(window,text=("your gess: ",runs,"computer guss: ",comp_bowl),bg="black", fg='light green')
            hello.place(x=800,y=70)
            hello1 = Label(window, text=("you are out: ",your_runs), bg="black", fg='light green')
            hello1.place(x=800, y=100)
            break
        elif runs > 10:
            hello2 = Label(window, text=("ALERT!! Support No only till 10"), bg="black", fg='light green')
            hello2.place(x=800, y=50)
            continue
        else:
            your_runs = your_runs + runs
            hello = Label(window, text=("your gess: ", runs, "computer guss: ", comp_bowl), bg="black", fg='light green')
            hello.place(x=800, y=70)
            hello1 = Label(window, text=("you runs now are: ", your_runs), bg="black", fg='light green')
            hello1.place(x=800, y=100)

            no_of_chances_1 = no_of_chances_1 + 1
            print("your 20 bowls are completed")
    label99 = Label(window, text=("your out  ","target:",your_runs), font="times 28 bold")
    label99.place(x=600, y=150, anchor="center")



    lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#list 2 for 2nd batting

    chances_2 = 20
    no_of_chances_2 = 0
    comp_runs = 0
    print("-----------------------------------------------")
    print("Computer Batting-\n")
    label89 = Label(window, text="your bowling", font="times 28 bold")
    label89.place(x=600, y=600, anchor="center")
    while no_of_chances_2 < chances_2: #1<20

        bowl = simpledialog.askinteger('input box', 'enter the runs')
        img107 = ImageTk.PhotoImage(Image.open("D:/hands/" + str(bowl) + ".jpeg"))
        my_label87 = Label(image=img107)
        my_label87.place(x=100, y=200)
        comp_bat = random.choice(lst2)
        img13 = ImageTk.PhotoImage(Image.open("D:/hands/" + str(comp_bat) + ".jpeg"))
        my_label14 = Label(image=img1)
        my_label14.place(x=800, y=200)

        if comp_bat == bowl:
            hello=Label(window,text=("computer guss: ",comp_bat,"your guss: ",bowl),bg="black", fg='light green')
            hello.place(x=800,y=20)
            hello1 = Label(window, text=("computer is out: ",comp_runs), bg="black", fg='light green')
            hello1.place(x=800, y=50)
            break
        else:
            comp_runs = comp_runs + comp_bat #0=0+7
            hello = Label(window, text=("computer guss: ", comp_bat, "your guss:", bowl), bg="black", fg='light green')
            hello.place(x=800, y=100)
            hello1 = Label(window, text=("computer run: ", comp_runs), bg="black", fg='light green')
            hello1.place(x=800, y=100)

            if comp_runs > your_runs: #7 > my target
                break

        no_of_chances_2 = no_of_chances_2 + 1 #0=0+1(1)

    print("\n-----------------------------------------------\nRESULTS: ")

    if comp_runs < your_runs:
        top = Toplevel()
        #bg = ImageTk.PhotoImage(Image.open("D:/numberplate/cricket.jpeg"))
        myLable2 = Label(top, image=bg1)
        myLable2.pack(padx=0, pady=0)
        Label10 = Label(top, text="Match result", font="Rockwell 24 bold", bg='#104E8B', fg='white')
        Label10.place(x=600, y=25, anchor="center")
        label999 = Label(top, text=("total runs:", your_runs,"cpm run",comp_runs,"\nyou won the game"), font="times 28 bold")
        label999.place(x=600, y=400, anchor="center")

    elif comp_runs == your_runs:
        print("The Game is a Tie")
        label997 = Label(window, text=("game is tie"),
                         font="times 28 bold",bg='green')
        label997.place(x=600, y=500, anchor="center")

    else:
        top = Toplevel()
        myLable2 = Label(top, image=bg1)
        myLable2.pack(padx=0, pady=0)
        Label10 = Label(top, text="Hand cricket", font="Rockwell 24 bold", bg='#104E8B', fg='white')
        Label10.place(x=600, y=25, anchor="center")
        label999 = Label(top, text=("total runs:", your_runs,"cpm run",comp_runs,"\ncomputer won the game"), font="times 28 bold")
        label999.place(x=600, y=400, anchor="center")
def function1():
    lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chances_2 = 20
    no_of_chances_2 = 0
    comp_runs = 0
    label89 = Label(window, text="your bowling", font="times 28 bold")
    label89.place(x=600, y=600, anchor="center")

    while no_of_chances_2 < chances_2:
        bowl = simpledialog.askinteger('input box', 'enter the runs')
        img101 = ImageTk.PhotoImage(Image.open("D:/hands/"+str(bowl)+".jpeg"))
        my_label1 = Label(image=img101)
        my_label1.place(x=100, y=200)
        comp_bat = random.choice(lst2)
        img10 = ImageTk.PhotoImage(Image.open("D:/hands/" + str(comp_bat) + ".jpeg"))
        my_label14 = Label(image=img10)
        my_label14.place(x=800, y=200)

        if bowl == comp_bat:
            hello=Label(window,text=("computer gess: ",comp_bat,"your guss: ",bowl),bg="black", fg='light green')
            hello.place(x=800,y=70)
            hello1 = Label(window, text=("computer are out: ",comp_runs), bg="black", fg='light green')
            hello1.place(x=800, y=100)
            break
        elif bowl > 10:
            hello2 = Label(window, text=("ALERT!! Support No only till 10"), bg="black", fg='light green')
            hello2.place(x=800, y=50)
            continue
        else:
            comp_runs = comp_runs + comp_bat
            hello = Label(window, text=("computer gess: ", comp_bat, "your guss: ", bowl), bg="black", fg='light green')
            hello.place(x=800, y=70)
            hello1 = Label(window, text=("computer runs now are: ", comp_runs), bg="black", fg='light green')
            hello1.place(x=800, y=100)

            no_of_chances_2 = no_of_chances_2 + 1
            print("your 20 bowls are completed")
    label99 = Label(window, text=("computer is out  ","target:",comp_runs), font="times 28 bold")
    label99.place(x=600, y=150, anchor="center")



    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#list 2 for 2nd batting

    chances_1 = 20
    no_of_chances_1 = 0
    your_runs = 0
    print("-----------------------------------------------")
    print("Computer Batting-\n")
    label89 = Label(window, text="your batting", font="times 28 bold")
    label89.place(x=600, y=600, anchor="center")
    while no_of_chances_1 < chances_1: #1<20

        runs = simpledialog.askinteger('input box', 'enter the runs')
        img107 = ImageTk.PhotoImage(Image.open("D:/hands/" + str(runs) + ".jpeg"))
        my_label87 = Label(image=img107)
        my_label87.place(x=100, y=200)
        comp_bowl = random.choice(lst1)
        img13 = ImageTk.PhotoImage(Image.open("D:/hands/" + str(comp_bowl) + ".jpeg"))
        my_label14 = Label(image=img13)
        my_label14.place(x=800, y=200)

        if runs == comp_bowl:
            hello=Label(window,text=("your guss: ",runs,"computer guss: ",comp_bowl),bg="black", fg='light green')
            hello.place(x=800,y=20)
            hello1 = Label(window, text=("your is out: ",your_runs), bg="black", fg='light green')
            hello1.place(x=800, y=50)
            break
        else:
            your_runs = your_runs + runs
            hello = Label(window, text=("your guss: ", runs, "computer guss:", comp_bowl), bg="black", fg='light green')
            hello.place(x=800, y=100)
            hello1 = Label(window, text=("your run: ", your_runs), bg="black", fg='light green')
            hello1.place(x=800, y=100)

            if comp_runs > your_runs: #7 > my target
                break

        no_of_chances_2 = no_of_chances_2 + 1 #0=0+1(1)

    print("\n-----------------------------------------------\nRESULTS: ")

    if comp_runs < your_runs:
        top = Toplevel()
        #bg = ImageTk.PhotoImage(Image.open("D:/numberplate/cricket.jpeg"))
        myLable2 = Label(top, image=bg1)
        myLable2.pack(padx=0, pady=0)
        Label10 = Label(top, text="Match result", font="Rockwell 24 bold", bg='#104E8B', fg='white')
        Label10.place(x=600, y=25, anchor="center")
        label999 = Label(top, text=("total runs:", your_runs,"cpm run",comp_runs,"\nyou won the game"), font="times 28 bold")
        label999.place(x=600, y=400, anchor="center")

    elif comp_runs == your_runs:
        print("The Game is a Tie")
        label997 = Label(window, text=("game is tie"),
                         font="times 28 bold",bg='green')
        label997.place(x=600, y=500, anchor="center")

    else:
        top = Toplevel()
        myLable2 = Label(top, image=bg1)
        myLable2.pack(padx=0, pady=0)
        Label10 = Label(top, text="Hand cricket", font="Rockwell 24 bold", bg='#104E8B', fg='white')
        Label10.place(x=600, y=25, anchor="center")
        label999 = Label(top, text=("total runs:", your_runs,"cpm run",comp_runs,"\ncomputer won the game"), font="times 28 bold")
        label999.place(x=600, y=400, anchor="center")


def tossh():
    top = Toplevel()

    def coinput():
        def entryon():
            if (editor4.get() == cointoss()):
                hello0 = Label(top, text="you won the toss", bg="black", fg='light green', font="times 28 bold")
                hello0.place(x=450, y=400)

                options = [
                    "batting",
                    "bowling",
                ]


                clicked = StringVar()
                clicked.set("batting")
                drop = OptionMenu(top, clicked, *options)
                drop.place(x=100,y=100)
                text = clicked.get()
                def clicked():
                    if ( text == "batting"):
                        print(function())
                    elif (text == "bowling"):
                        print(function1())
                    else:
                        print("you have entered invalid choice")
                        return None

                play347 = Button(top, text=" next ", font=("Impact", 20), anchor="center", bg='green', fg='white',
                                 command=clicked)
                play347.place(x=750, y=550)

            else:
                hello0 = Label(top, text="you lost the toss", bg="black", fg='light green', font="times 28 bold")
                hello0.place(x=450, y=400)
                play347 = Button(top, text=" next ", font=("Impact", 20), anchor="center", bg='green', fg='white',command=function)
                play347.place(x=750, y=550)


        editor4 = Entry(top, textvariable=language_var, bg="white", fg='black', font=27, )
        editor4.place(x=500, y=500)
        play344 = Button(top, text=" TOSS ", font=("Impact", 20), anchor="center", bg='green', fg='white',command=entryon)
        play344.place(x=550, y=550)


    myLable2 = Label(top, image=bg1)
    myLable2.pack(padx=0, pady=0)
    Label10 = Label(top, text="Hand cricket", font="Rockwell 24 bold", bg='#104E8B', fg='white')
    Label10.place(x=600, y=25, anchor="center")
    Label19 = Label(top, text="Click Continue to get the Toss option", font="Rockwell 24 bold", bg='#104E8B', fg='white')
    Label19.place(x=600, y=350, anchor="center")
    play34 = Button(top, text=" Continue ", font=("Impact", 20), anchor="center", bg='green', fg='white', command=coinput)
    play34.place(x=550, y=200)

bg1 = ImageTk.PhotoImage(Image.open("D:/numberplate/QT-Cricket.jpg"))
play = Button(window,text=" START ",font=("Impact", 20),anchor="center",bg='green',fg='white',command=tossh)
play.place(x=550,y=200)

play = Button(window,text=" PLAY NOW ",font=("Impact", 30),anchor="center",bg='black',fg='white',command=function)
play.place(x=500,y=300)


window.mainloop()
