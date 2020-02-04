from tkinter import *
from random import randint
import time

window = Tk()
canvas = Canvas(window, width=400, height=400)
canvas.pack()


def makeArr(size):
    arr = []
    i = 0
    while (i < size):
        arr.append(randint(20, 400))
        i += 1
    return arr


# print (makeArr(20))

def createArr(arr, a = None, b = None):
    i = 0
    while (i < len(arr)):
        if (i == a or i == b):
            canvas.create_rectangle(i * 10, 0, i * 10 + 10, arr[i], fill="yellow")
        else:
            canvas.create_rectangle(i * 10, 0, i * 10 + 10, arr[i], fill="blue")
        i += 1


def insertionSort(arr):
    createArr(arr)
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            canvas.delete("all")
            createArr(arr,i,j)
            window.update()
            time.sleep(.1)
        arr[j + 1] = key
    createArr(arr)

button1 = Button(window, text = "Stop", command = window.destroy)
button1.pack()
a = makeArr(40)
insertionSort(a)


# canvas.create_rectangle(0,0,50,50, fill='blue')
#window.after(5000,window.destroy)

mainloop()
