import random
import tkinter as tk

root = tk.Tk()
root.geometry("600x500")
root.title("Sten Sax Påse")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""


def choice_to_number(choice):
    ssp = {'sten': 0, 'påse': 1, 'sax': 2}
    return ssp[choice]


def number_to_choice(number):
    ssp = {0: 'sten', 1: 'påse', 2: 'sax'}
    return ssp[number]


def random_computer_choice():
    return random.choice(['sten', 'påse', 'sax'])


def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if (user == comp):
        print("Lika")
    elif ((user-comp) % 3 == 1):
        print("Du vann")
        USER_SCORE += 1
    else:
        print("Datorn vann")
        COMP_SCORE += 1

    text_area = tk.Text(master=root, height=10, width=35, bg="yellow")
    text_area.grid(column=2, row=2)
    answer = "Ditt val: {uc} \n\nDatorns val: {cc} \n\nDin poäng: {u} \n\nDatorns poäng: {c} ".format(
        uc=USER_CHOICE, cc=COMP_CHOICE, u=USER_SCORE, c=COMP_SCORE)
    text_area.insert(tk.END, answer)
    if (user == comp):
        text_area.insert(tk.END, "\n\nLika")
    elif ((user-comp) % 3 == 1):
        text_area.insert(tk.END, "\n\nDu vann")
    else:
        text_area.insert(tk.END, "\n\nDatorn vann")


def sten():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'sten'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def sax():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'sax'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def påse():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'påse'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


b1 = tk.Button(text="       Sten       ", bg="red", command=sten)
b1.grid(column=1, row=0, padx=40, pady=40)
b2 = tk.Button(text="       Sax        ", bg="blue", command=sax)
b2.grid(column=2, row=0, padx=40, pady=40)
b3 = tk.Button(text="       Påse       ", bg="lightgreen", command=påse)
b3.grid(column=3, row=0, padx=40, pady=40)

root.mainloop()
