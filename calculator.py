from tkinter import *

hl_okno=Tk()      
hl_okno.title("Calculator")
hl_okno.resizable(0, 0)

number1 = ""
number2 = ""
operation = ""
result = 0

def count1(): #řeší operace
    global number1, number2, operation,result
    if operation == "+":
        result = int(number1) + int(number2)
    elif operation == "-":
        result = int(number1) - int(number2)
    elif operation == "x":
        result = int(number1) * int(number2)
    elif operation == "/":
        result = int(number1) / int(number2)
    input1.delete(0, END) #vyčistění pole pro zadání druhého čísla
    input1.insert(0, str(result))
    number1 = str(result) #uloží výsledek, jako číslo 1 pro další počítání
    number2 = ""

def classify_number(number):
    global number1, number2, operation
    if operation == "":
        number1 +=str(number)
        input1.delete(0, END)
        input1.insert(0, number1)
    else:
        number2 += str(number)
        input1.delete(0, END)
        input1.insert(0, number2)

def classify_operation(oper): #při stisku +,-,x,/, nastaví proměnnou operation na příslušnou hodnotu
    global number1, operation, result
    if number1 and number2:
        count1()
    operation = oper

def delete_it(): #funkce klávesy C
    global number1, number2, operation, result
    input1.delete(0,END)
    number1 = ""
    number2 = ""
    operation = ""
    result = ""
    
jmeno=Label(hl_okno, text="Always work with two nubers: ",font=("Arial",14))
jmeno.grid(row=0,columnspan=4) 
#1 řádek--------------------------------------------------------------------------
input1=Entry(hl_okno,width=10) #pole obrazovky
input1.grid(row=1,columnspan=4,sticky=W+E)  
#2 řádek--------------------------------------------------------------------------
t1=Button(hl_okno,text="7",width=4, command = lambda: classify_number(7))
t1.grid(row=2,column=0)

t2=Button(hl_okno,text="8",width=4, command = lambda: classify_number(8))
t2.grid(row=2,column=1)

t3=Button(hl_okno,text="9",width=4, command = lambda: classify_number(9))
t3.grid(row=2,column=2)

tplus=Button(hl_okno,text="+",width=4, command = lambda: classify_operation("+"))
tplus.grid(row=2,column=3)
#3 řádek--------------------------------------------------------------------------
t4=Button(hl_okno,text="4",width=4, command = lambda: classify_number(4))
t4.grid(row=3,column=0)

t5=Button(hl_okno,text="5",width=4, command = lambda: classify_number(5))
t5.grid(row=3,column=1)

t6=Button(hl_okno,text="6",width=4, command = lambda: classify_number(6))
t6.grid(row=3,column=2)

tminus=Button(hl_okno,text="-",width=4, command=lambda: classify_operation("-"))
tminus.grid(row=3,column=3)
#4 řádek--------------------------------------------------------------------------
t7=Button(hl_okno,text="1",width=4, command = lambda: classify_number(1))
t7.grid(row=4,column=0)

t8=Button(hl_okno,text="2",width=4, command = lambda: classify_number(2))
t8.grid(row=4,column=1)

t9=Button(hl_okno,text="3",width=4, command = lambda: classify_number(3))
t9.grid(row=4,column=2)

trovno=Button(hl_okno,text="x",width=4, command=lambda: classify_operation("x"))
trovno.grid(row=4,column=3)
#5 řádek--------------------------------------------------------------------------

t10=Button(hl_okno,text="0",width=4, command = lambda: classify_number(0))
t10.grid(row=5,column=0)

t12=Button(hl_okno,text="C",width=4, command = delete_it)
t12.grid(row=5,column=1 )

rovno=Button(hl_okno,text="=",width=4, command = count1)
rovno.grid(row=5, column=2)

t13=Button(hl_okno,text="/",width=4, command=lambda: classify_operation("/"))
t13.grid(row=5,column=3)

#--------------------------------------------------------------------------
hl_okno.mainloop()              