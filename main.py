import random;
from tkinter import *
from tkinter import messagebox
from turtle import clear

if __name__ == "__main__":

    # making of the GUI
    gui = Tk()
    gui.title("PassPao")
    gui.geometry("300x400")
    gui.config(background="black")
    gui.resizable(0,0)

    def shuffle(list):
        tempList = list
        random.shuffle(tempList)
        return ''.join(tempList)
    def passpao():
        output_lable2 = Label(gui, text="                ", font="Cascadia_Code 12 ", bg="black", fg="white")
        output_lable2.place(x=150,y=320)
        nUpper =   nuc.get()
        nLower =   nlc.get() 
        nSpecial =  nsc.get()
        nNumeric =  nnc.get() 

        if nUpper == "" or nLower == "" or nSpecial == "" or  nNumeric == "":
          messagebox.showerror("Warning", "All fields are required!!!")
        else:
            intnUpper = int(float(nuc.get()))
            intnLower = int(float(nlc.get()))
            intnSpecial = int(float(nsc.get()))
            intnNumeric = int(float(nnc.get()))
        upperCase = []
        lowerCase = []
        specialChar = []
        numericDigits = []
        for u in range(intnUpper):
            upperCase.append(chr(random.randint(65,90)))
        for l in range(intnLower):
            lowerCase.append(chr(random.randint(97,122)))
        for s in range(intnSpecial):
            specialChar.append(chr(random.randint(32,47)))
        for n in range(intnNumeric):
            numericDigits.append(chr(random.randint(48,57)))
        password =  upperCase + lowerCase + specialChar + numericDigits
        password = shuffle(password)
        output_lable = Label(gui, text=password, font="Cascadia_Code 12 ", bg="black", fg="white")
        output_lable.place(x=150,y=320)
         
        def exit():
            quit()

       

    # label 0 application name
    gui_lable0 = Label(gui, text='''PassPao''', font="NSimSun 17 bold italic", bg="black",height=2,width=500,fg="LightGrey")
    gui_lable0.pack()
    #label 1 No. of uppercase letters
    gui_lable1 = Label(gui, text="No. of Uppercase Letters", font="Cascadia_Code 12 ", bg="black", fg="lightgrey")
    gui_lable1.place(x=20,y=70)
    #entry 1
    nuc = Entry(gui, width=4, font="Ariel 12 italic", bg="white")
    nuc.place(x=240,y=70)
    #label 2 No. of lowercase letters
    gui_lable2 = Label(gui, text="No. of Lowercase Letters", font="Cascadia_Code 12 ", bg="black", fg="lightgrey")
    gui_lable2.place(x=20,y=100)
    #entry 2
    nlc = Entry(gui, width=4, font="Ariel 12 italic", bg="white")
    nlc.place(x=240,y=100)
    #label 3 No. of  special characters
    gui_lable3 = Label(gui, text="No. of Special Characters", font="Cascadia_Code 12 ", bg="black", fg="lightgrey")
    gui_lable3.place(x=20,y=130)
    #entry 3
    nsc = Entry(gui, width=4, font="Ariel 12 italic", bg="white")
    nsc.place(x=240,y=130)
    #label 4 No. of numeric digits
    gui_lable4 = Label(gui, text="No. of Numeric Digits", font="Cascadia_Code 12 ", bg="black", fg="lightgrey")
    gui_lable4.place(x=20,y=160)
    #entry 4
    nnc = Entry(gui, width=4, font="Ariel 12 italic", bg="white")
    nnc.place(x=240,y=160)
    # get password button
    getpass = Button(gui, text="GET MY PASSWORD !!!!", bg="lightblue", font="Ariel 14 ", width=23, command= passpao ) 
    getpass.place(x=20,y=250)
    #password lable text
    output_lable1 = Label(gui, text="Your Password: ", font="Cascadia_Code 12 ", bg="black", fg="lightgrey")
    output_lable1.place(x=20,y=320)
     # Exit button
    getpass = Button(gui, text="Exit", bg="red", font="Ariel 14 ", width=5, command= exit ) 
    getpass.place(x=20,y=350)
    gui.mainloop()