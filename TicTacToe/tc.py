from tkinter import *
import tkinter.messagebox

tk = Tk()#creates window
tk.title("Tic Tac Toe Multiplayer")#Title

# String variables for player names
playerA = StringVar()
playerB = StringVar()
p1 = StringVar()
p2 = StringVar()

# Entry widgets for player names
player1_name = Entry(tk, textvariable=p1, bd=5)#bd border length
player1_name.grid(row=1, column=1, columnspan=8)

player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

def disableButton():
    """Disable all buttons after game ends."""
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)

def btnClick(button):
    """Handle button click events."""
    global bclick, flag
    if button["text"] == " ":
        if bclick:
            button["text"] = "X"
            bclick = False
        else:
            button["text"] = "O"
            bclick = True
        checkforwin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Button already clicked")

def checkforwin():
    """Check for a win or tie condition."""
    win_conditions = [
        (button1, button2, button3),
        (button4, button5, button6),
        (button7, button8, button9),
        (button1, button5, button9),
        (button3, button5, button7),
        (button1, button4, button7),
        (button2, button5, button8),
        (button3, button6, button9)
    ]

    for condition in win_conditions:
        if condition[0]['text'] == condition[1]['text'] == condition[2]['text'] and condition[0]['text'] != " ":
            winner = condition[0]['text']
            if winner == "X":
                tkinter.messagebox.showinfo("Tic Tac Toe", p1.get() + " Wins!")
            else:
                tkinter.messagebox.showinfo("Tic Tac Toe", p2.get() + " Wins!")
            disableButton()
            return

    if flag == 8:
        tkinter.messagebox.showinfo("Tic Tac Toe", "It's a tie")
        disableButton()

# Create labels for player names
Label(tk, text="Player 1:", font="Times 20 bold", bg="white", fg='black', height=1, width=8).grid(row=1, column=0)
Label(tk, text="Player 2:", font="Times 20 bold", bg="white", fg='black', height=1, width=8).grid(row=2, column=0)

# Create buttons for the Tic Tac Toe board
button1 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
