
from tkinter import *
from tkinter import filedialog, messagebox
import random
import time
import requests



# Functions

def reset():
    textReceipt.delete(1.0, END)
    e_roti.set('0')
    e_daal.set('0')
    e_fish.set('0')


    e_soda.set('0')
    e_coffee.set('0')
    e_faluda.set('0')


    e_kitkat.set('0')
    e_oreo.set('0')
    e_apple.set('0')

    e_meat.set('0')
    e_beans.set('0')
    e_vegetables.set('0')


    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textfish.config(state=DISABLED)


    textsoda.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textfaluda.config(state=DISABLED)


    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)

    textmeat.config(state=DISABLED)
    textbeans.config(state=DISABLED)
    textvegetables.config(state=DISABLED)


    var1.set(0)
    var2.set(0)
    var3.set(0)

    var10.set(0)
    var11.set(0)
    var12.set(0)

    var19.set(0)
    var20.set(0)
    var21.set(0)

    var28.set(0)
    var29.set(0)
    var30.set(0)


    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    costofsaucevar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

def receipt():
    global billnumber, date
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
        textReceipt.insert(END, '***************************************************************\n')
        textReceipt.insert(END, 'Items:\t\t Cost Of Items(ksh)\n')
        textReceipt.insert(END, '***************************************************************\n')
        if e_roti.get() != '0':
            textReceipt.insert(END, f'matoke\t\t\t{int(e_roti.get()) * 70}\n\n')

        if e_daal.get() != '0':
            textReceipt.insert(END, f'rice\t\t\t{int(e_daal.get()) * 120}\n\n')

        if e_fish.get() != '0':
            textReceipt.insert(END, f'posho\t\t\t{int(e_fish.get()) * 100}\n\n')




        if e_soda.get() != '0':
            textReceipt.insert(END, f'soda:\t\t\t{int(e_soda.get()) * 50}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'water:\t\t\t{int(e_coffee.get()) * 40}\n\n')

        if e_faluda.get() != '0':
            textReceipt.insert(END, f'juice:\t\t\t{int(e_faluda.get()) * 80}\n\n')



        if e_oreo.get() != '0':
            textReceipt.insert(END, f'coffee:\t\t\t{int(e_oreo.get()) * 400}\n\n')

        if e_apple.get() != '0':
            textReceipt.insert(END, f'milk:\t\t\t{int(e_apple.get()) * 300}\n\n')

        if e_kitkat.get() != '0':
            textReceipt.insert(END, f'black Tea:\t\t\t{int(e_kitkat.get()) * 500}\n\n')


        if e_meat.get() != '0':
            textReceipt.insert(END, f'meat:\t\t\t{int(e_meat.get()) * 400}\n\n')

        if e_beans.get() != '0':
            textReceipt.insert(END, f'beans:\t\t\t{int(e_beans.get()) * 300}\n\n')

        if e_vegetables.get() != '0':
            textReceipt.insert(END, f'vegetables:\t\t\t{int(e_vegetables.get()) * 500}\n\n')

        textReceipt.insert(END, '***************************************************************\n')
        if costoffoodvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')
        #if costofsaucevar.get() != '0 Rs':
          #  textReceipt.insert(END, f'Cost Of sauce\t\t\t{priceofsauce}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{5}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems + 5}Rs\n\n')
        textReceipt.insert(END, '***************************************************************\n')

    else:
        messagebox.showerror('Error', 'No Item Is selected')


def totalcost():
    global priceofFood, priceofDrinks, priceofCakes, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var10.get() != 0 or var11.get() != 0 or \
            var12.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var28.get() != 0 or \
            var29.get() != 0 or var30.get() != 0 or var13.get() != 0:


        item1 = int(e_roti.get())
        item2 = int(e_daal.get())
        item3 = int(e_fish.get())


        item10 = int(e_soda.get())
        item11 = int(e_coffee.get())
        item12 = int(e_faluda.get())


        item19 = int(e_oreo.get())
        item20 = int(e_apple.get())
        item21 = int(e_kitkat.get())

        item28 = int(e_meat.get())
        item29 = int(e_beans.get())
        item30 = int(e_vegetables.get())

        priceofFood = (item1 * 70) + (item2 * 120) + (item3 * 100)


        priceofDrinks = (item10 * 50) + (item11 * 40) + (item12 * 80)


        priceofCakes = (item19 * 400) + (item20 * 300) + (item21 * 500)

        priceofsauce = (item28* 400) + (item29 * 300) + (item30 * 500)


        costoffoodvar.set(str(priceofFood) + ' ksh')
        costofdrinksvar.set(str(priceofDrinks) + ' ksh')
        costofcakesvar.set(str(priceofCakes) + ' ksh')
        costofsaucevar.set(str(priceofsauce) + ' ksh')

        subtotalofItems = priceofFood + priceofDrinks + priceofCakes+priceofsauce
        subtotalvar.set(str(subtotalofItems) + ' ksh')

        servicetaxvar.set('5 ksh')

        tottalcost = subtotalofItems + 5
        totalcostvar.set(str(tottalcost) + 'ksh')

    else:
        messagebox.showerror('Error', 'No Item Is selected')


def roti():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.delete(0, END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')


def daal():
    if var2.get() == 1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0, END)
        textdaal.focus()

    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')


def fish():
    if var3.get() == 1:
        textfish.config(state=NORMAL)
        textfish.delete(0, END)
        textfish.focus()

    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')



def soda():
    if var10.get() == 1:
        textsoda.config(state=NORMAL)
        textsoda.focus()
        textsoda.delete(0, END)
    elif var10.get() == 0:
        textsoda.config(state=DISABLED)
        e_soda.set('0')


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def faluda():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.focus()
        textfaluda.delete(0, END)
    elif var12.get() == 0:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')





def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    elif var18.get() == 0:
        textcolddrinks.config(state=DISABLED)
        e_coldrinks.set('0')


def oreo():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    elif var19.get() == 0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


def apple():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    elif var20.get() == 0:
        textapple.config(state=DISABLED)
        e_apple.set('0')


def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')




def meat():
    if var28.get() == 1:
        textmeat.config(state=NORMAL)
        textmeat.focus()
        textmeat.delete(0, END)
    elif var25.get() == 0:
        textmeat.config(state=DISABLED)
        e_meat.set('0')


def beans():
    if var29.get() == 1:
        textbeans.config(state=NORMAL)
        textbeans.focus()
        textbeans.delete(0, END)
    elif var26.get() == 0:
        textbeans.config(state=DISABLED)
        e_beans.set('0')


def vegetables():
    if var30.get() == 1:
        textvegetables.config(state=NORMAL)
        textvegetables.focus()
        textvegetables.delete(0, END)
    elif var27.get() == 0:
        textvegetables.config(state=DISABLED)
        e_vegetables.set('0')


root = Tk()

root.geometry('1350x550+0+0')

root.resizable(0, 0)

root.title('Restaurant Management System created by clinton mogoi')

root.config(bg='grey')

topFrame = Frame(root, bd=10, relief=RIDGE, bg='grey')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='HOTEL MANAGEMENT SYSTEM', font=('arial', 30, 'bold'), fg='black', bd=10,
                   bg='grey', width=40)
labelTitle.pack()

# frames

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='grey')
menuFrame.place(x=1,y=120)


drinksFrame = LabelFrame(menuFrame, text='Cold Drinks', font=('arial', 19, 'bold'), bd=25, relief=RIDGE, fg='blue', )
drinksFrame.grid(row=0, column=0,sticky=W)

foodFrame = LabelFrame(menuFrame, text='Foods', font=('arial', 19, 'bold'), bd=25, relief=RIDGE, fg='blue')
foodFrame.grid(row=0, column=1,sticky=W)

cakesFrame = LabelFrame(menuFrame, text='Hot Drinks', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='blue')
cakesFrame.grid(row=1, column=0)

sauceFrame = LabelFrame(menuFrame, text='sauce', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='blue')
sauceFrame.grid(row=1, column=1)

rightFrame = Frame(root, bd=15, relief=RIDGE, bg='grey')
rightFrame.place(x=530,y=90)

calculatorFrame = Frame(rightFrame, bd=2, relief=RIDGE, bg='grey')
calculatorFrame.grid(row=0,column=1)

recieptFrame = Frame(rightFrame, bd=4, relief=RIDGE, bg='grey')
recieptFrame.grid(row=0, column=0)

buttonFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg='grey')
buttonFrame.grid(row=1, column=0,columnspan=2,sticky=W)

# Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13=IntVar()

var19 = IntVar()
var20 = IntVar()
var21 = IntVar()

var28 = IntVar()
var29 = IntVar()
var30 = IntVar()

e_roti = StringVar()
e_daal = StringVar()
e_fish = StringVar()


e_soda = StringVar()
e_coffee = StringVar()
e_faluda = StringVar()


e_oreo = StringVar()
e_apple = StringVar()
e_kitkat = StringVar()


e_meat=StringVar()
e_beans=StringVar()
e_vegetables=StringVar()

costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofcakesvar = StringVar()
costofsaucevar = StringVar()

subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

e_roti.set('0')
e_daal.set('0')
e_fish.set('0')


e_soda.set('0')
e_coffee.set('0')
e_faluda.set('0')


e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')


e_meat.set('0')
e_beans.set('0')
e_vegetables.set('0')

##FOOD

roti = Checkbutton(foodFrame, text='Matoke', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1
                   , command=roti)
roti.grid(row=0, column=0, sticky=W)

daal = Checkbutton(foodFrame, text='Rice', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2
                   , command=daal)
daal.grid(row=1, column=0, sticky=W)

fish = Checkbutton(foodFrame, text='Posho', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3
                   , command=fish)
fish.grid(row=2, column=0, sticky=W)


### SAUCE
meat= Checkbutton(sauceFrame, text='meat', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var28
                  , command=meat)
meat.grid(row=0,column=0, sticky=W)

beans= Checkbutton(sauceFrame, text='beans', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var29
                   , command=beans)
beans.grid(row=1,column=0, sticky=W)

vegetables= Checkbutton(sauceFrame, text='vegetables', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var30
                        , command=vegetables)
vegetables.grid(row=2,column=0, sticky=W)

##entry field for sauce
textmeat = Entry(sauceFrame, font=('arial', 18, 'bold'), bd=7, width=6,  textvariable=e_meat,bg='aqua')
textmeat.grid(row=0, column=1)

textbeans = Entry(sauceFrame, font=('arial', 18, 'bold'), bd=7, width=6,  textvariable=e_beans,bg='aqua')
textbeans.grid(row=1, column=1)

textvegetables = Entry(sauceFrame, font=('arial', 18, 'bold'), bd=7, width=6,  textvariable=e_vegetables,bg='aqua')
textvegetables.grid(row=2, column=1)



# Entry Fields for Food Items

textroti = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6,  textvariable=e_roti,bg='aqua')
textroti.grid(row=0, column=1)

textdaal = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, textvariable=e_daal,bg='aqua')
textdaal.grid(row=1, column=1)

textfish = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6,  textvariable=e_fish,bg='aqua')
textfish.grid(row=2, column=1)



# Drinks

soda = Checkbutton(drinksFrame, text='Soda', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var11
                    , command=soda)
soda.grid(row=0, column=0, sticky=W)

coffee = Checkbutton(drinksFrame, text='Water', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var12
                     , command=coffee)
coffee.grid(row=1, column=0, sticky=W)

faluda = Checkbutton(drinksFrame, text='Juice', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var13
                     , command=faluda)
faluda.grid(row=2, column=0, sticky=W)



# entry fields for drink items

textsoda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6,  textvariable=e_soda,bg='aqua')
textsoda.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6,  textvariable=e_coffee,bg='aqua')
textcoffee.grid(row=1, column=1)

textfaluda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, textvariable=e_faluda,bg='aqua')
textfaluda.grid(row=2, column=1)



# Cakes

oreocake = Checkbutton(cakesFrame, text='Coffee', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var19
                       , command=oreo)
oreocake.grid(row=0, column=0, sticky=W)

applecake = Checkbutton(cakesFrame, text='Milk', font=('arial', 18, 'bold'),onvalue=1, offvalue=0, variable=var20
                        , command=apple)
applecake.grid(row=1, column=0, sticky=W)

kitkatcake = Checkbutton(cakesFrame, text='Black Tea', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var21
                         , command=kitkat)
kitkatcake.grid(row=2, column=0, sticky=W)



# entry fields for cakes

textoreo = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, textvariable=e_oreo,bg='aqua')
textoreo.grid(row=0, column=1)

textapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6,  textvariable=e_apple,bg='aqua')
textapple.grid(row=1, column=1)

textkitkat = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6,  textvariable=e_kitkat,bg='aqua')
textkitkat.grid(row=2, column=1)

# Buttons
labelServiceTax = Label(buttonFrame, text='Tax', font=('arial', 18, 'bold'), bg='firebrick4', fg='white',bd=5,padx=1)
labelServiceTax.grid(row=0, column=0,sticky=W)

buttonServiceTax = Button(buttonFrame,font=('arial', 14, 'bold'), bd=6, width=12,bg='aqua',
                       textvariable=servicetaxvar)
buttonServiceTax.grid(row=0, column=1,columnspan=2)

buttonTotal = Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=6,pady=7,
                     command=totalcost)
buttonTotal.grid(row=1, column=0,sticky=W)
textSubTotal = Entry(buttonFrame, font=('arial', 16, 'bold'), bd=6, width=12,textvariable=subtotalvar,bg='aqua')
textSubTotal.grid(row=1, column=1,columnspan=2)

buttonReceipt = Button(buttonFrame, text='print Receipt', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5
                       , command=receipt)
buttonReceipt.grid(row=2, column=0,sticky=W)


buttonReset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5,
                     command=reset)
buttonReset.grid(row=2, column=1,sticky=W)

# textarea for receipt

textReceipt = Text(recieptFrame, font=('arial', 12, 'bold'), bd=3, width=38, height=14)
textReceipt.grid(row=0, column=4)

# Calculator
operator = ''  # 7+9


def buttonClick(numbers):  # 9
    global operator
    operator = operator + numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)


def clear():
    global operator
    operator = ''
    calculatorField.delete(0, END)


def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0, result)
    operator = ''


calculatorField = Entry(calculatorFrame, font=('arial', 16, 'bold'),bg='yellow', width=32, bd=4)
calculatorField.grid(row=0, column=0, columnspan=4)

button7 = Button(calculatorFrame, text='7', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6,
                 command=lambda: buttonClick('7'))
button7.grid(row=1, column=0)

button8 = Button(calculatorFrame, text='8', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6,
                 command=lambda: buttonClick('8'))
button8.grid(row=1, column=1)

button9 = Button(calculatorFrame, text='9', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                 , command=lambda: buttonClick('9'))
button9.grid(row=1, column=2)

buttonPlus = Button(calculatorFrame, text='+', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                    , command=lambda: buttonClick('+'))
buttonPlus.grid(row=1, column=3)

button4 = Button(calculatorFrame, text='4', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                 , command=lambda: buttonClick('4'))
button4.grid(row=2, column=0)

button5 = Button(calculatorFrame, text='5', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                 , command=lambda: buttonClick('5'))
button5.grid(row=2, column=1)

button6 = Button(calculatorFrame, text='6', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                 , command=lambda: buttonClick('6'))
button6.grid(row=2, column=2)

buttonMinus = Button(calculatorFrame, text='-', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                     , command=lambda: buttonClick('-'))
buttonMinus.grid(row=2, column=3)

button1 = Button(calculatorFrame, text='1', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                 , command=lambda: buttonClick('1'))
button1.grid(row=3, column=0)

button2 = Button(calculatorFrame, text='2', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                 , command=lambda: buttonClick('2'))
button2.grid(row=3, column=1)

button3 = Button(calculatorFrame, text='3', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                 , command=lambda: buttonClick('3'))
button3.grid(row=3, column=2)

buttonMult = Button(calculatorFrame, text='*', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                    , command=lambda: buttonClick('*'))
buttonMult.grid(row=3, column=3)

buttonAns = Button(calculatorFrame, text='Ans', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6,
                   command=answer)
buttonAns.grid(row=4, column=0)

buttonClear = Button(calculatorFrame, text='Clear', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                     , command=clear)
buttonClear.grid(row=4, column=1)

button0 = Button(calculatorFrame, text='0', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6
                 , command=lambda: buttonClick('0'))
button0.grid(row=4, column=2)

buttonDiv = Button(calculatorFrame, text='/', font=('arial', 16, 'bold'), fg='black', bg='grey', bd=6, width=6,
                   command=lambda: buttonClick('/'))
buttonDiv.grid(row=4, column=3)

root.mainloop()