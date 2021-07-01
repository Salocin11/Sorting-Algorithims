import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class Sorts(object):
    def __init__(self, data):
        Sorts.original = data
        Sorts.data = data

    def swap(self, a, b):
        Sorts.data[a], Sorts.data[b] = Sorts.data[b], Sorts.data[a]

    def bubblesort(self):  # Checks adjacent numbers and swaps
        for i in range(len(Sorts.data)):
            for y in range(0, len(Sorts.data) - i - 1):
                if Sorts.data[y] > Sorts.data[y + 1]:
                    Sorts.swap(Sorts, y, y + 1)
                yield Sorts.data
        print(Sorts.data)

    def selectionsort(self):  # Brings lowest to bottom of list.
        for i in range(len(Sorts.data)):
            min = i
            for j in range(i + 1, len(Sorts.data)):
                if Sorts.data[min] > Sorts.data[j]:
                    min = j
            Sorts.swap(Sorts, i, min)
            yield Sorts.data
        print(Sorts.data)

    def insertionsort(self):
        for i in range(1, len(Sorts.data)):
            key = Sorts.data[i]
            j = i - 1
            while j >= 0 and key < Sorts.data[j]:
                Sorts.data[j + 1] = Sorts.data[j]
                j -= 1
            Sorts.data[j + 1] = key
            yield Sorts.data
        print(Sorts.data)

    def mergesort(self):
        pass


# Tkinter Interface

# Create Menu
root = tk.Tk()
menu = tk.Canvas(root, width=350, height=350, bg='lightsteelblue2', relief='raised')
menu.pack()

# Title of Canvas
label1 = tk.Label(root, text='  Sorting Algo Visualised', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
menu.create_window(150, 60, window=label1)


# Select Data Button

def datapopup():
    # Create Dataset Menu
    dataMenu = tk.Tk()
    dataMenu = tk.Canvas(dataMenu, width=350, height=350, bg='lightsteelblue2', relief='raised')
    dataMenu.pack()

    # Create List of Datasets

    # Random Data
    def select_randomData():
        global str_data
        str_data = []
        for i in range(100):
            str_data.append(random.randint(1, 200))

    selectRandomDataButton = tk.Button(dataMenu, text="     Random Data     ", command=select_randomData, bg='green',
                                       fg='white',
                                       font=('helvetica', 12, 'bold'))
    dataMenu.create_window(150, 130, window=selectRandomDataButton)

    def select_reverseData():
        global str_data
        str_data = []
        for i in range(200, -1, -1):
            str_data.append(i)

    selectReverseDataButton = tk.Button(dataMenu, text="     Reverse Data     ", command=select_reverseData, bg='green',
                                        fg='white',
                                        font=('helvetica', 12, 'bold'))
    dataMenu.create_window(150, 180, window=selectReverseDataButton)


selectDataButton = tk.Button(text="     Select Data     ", command=datapopup, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
menu.create_window(150, 130, window=selectDataButton)


# Select Sort Algorithim
def algopopup():
    # Create Sort Algo Menu
    algoMenu = tk.Tk()
    algoMenu = tk.Canvas(algoMenu, width=350, height=350, bg='lightsteelblue2', relief='raised')
    algoMenu.pack()

    # Create List of Sort Algo

    # Bubble Sort
    def select_bubblesort():
        global algo
        algo = "Bubble Sort"
        print("Bubble Sort selected")

    selectBubbleButton = tk.Button(algoMenu, text="     Bubble Sort     ", command=select_bubblesort, bg='green',
                                   fg='white',
                                   font=('helvetica', 12, 'bold'))
    algoMenu.create_window(150, 130, window=selectBubbleButton)

    # Selection Sort
    def select_Selectsort():
        global algo
        algo = "Selection Sort"
        print("Selection Sort selected")

    selectSelectButton = tk.Button(algoMenu, text="     Selection Sort     ", command=select_Selectsort, bg='green',
                                   fg='white',
                                   font=('helvetica', 12, 'bold'))
    algoMenu.create_window(150, 180, window=selectSelectButton)

    # Insertion Sort
    def select_Insertsort():
        global algo
        algo = "Insertion Sort"
        print("Insertion Sort selected")

    selectInsertButton = tk.Button(algoMenu, text="     Insertion Sort     ", command=select_Insertsort, bg='green',
                                   fg='white',
                                   font=('helvetica', 12, 'bold'))
    algoMenu.create_window(150, 230, window=selectInsertButton)


selectAlgoButton = tk.Button(text="     Select Algo     ", command=algopopup, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
menu.create_window(150, 180, window=selectAlgoButton)


# Run Application
def run():
    # Plotting Code
    abc = Sorts(str_data)
    fig, ax = plt.subplots()
    ax.set_title(algo)

    bar_rec = ax.bar(range(len(abc.data)), abc.data, align='edge')

    ax.set_xlim(0, 200)
    ax.set_ylim(0, int(200 * 1.1))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    operations = [0]

    def update_plot(array, rec, operations):
        for rec, val in zip(rec, array):
            rec.set_height(val)
        operations[0] += 1
        text.set_text("No.of operations :{}".format(operations[0]))

    if algo == "Bubble Sort":
        anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, operations), frames=abc.bubblesort(),
                                   interval=1,
                                   repeat=False)
    elif algo == "Selection Sort":
        anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, operations), frames=abc.selectionsort(),
                                   interval=1,
                                   repeat=False)
    elif algo == "Insertion Sort":
        anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, operations), frames=abc.insertionsort(),
                                   interval=1,
                                   repeat=False)

    plt.show()


runButton = tk.Button(text='Run Application', command=run, bg='green', fg='white', font=('helvetica', 12, 'bold'))
menu.create_window(150, 230, window=runButton)


# Exit Application

def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='Exit Application', command=exitApplication, bg='brown', fg='white',
                       font=('helvetica', 12, 'bold'))
menu.create_window(150, 280, window=exitButton)

# Stop TKinter from closing

root.mainloop()
