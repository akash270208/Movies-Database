import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import messagebox
import movies_database as db


mainWindow = tk.Tk()
mainWindow.title("  Movie Record Window ")
mainWindow.geometry("550x250")
mainWindow.resizable(0, 0)

tk.Label(mainWindow, text="Movie Name").place(x=30, y=30)
name = tk.Entry(mainWindow, width=50)
name.place(x=120, y=30)

tk.Label(mainWindow, text="Movie Duration").place(x=30, y=60)
duration1 = ttk.Combobox(mainWindow, width=10)
duration1['values'] = (0, 1, 2, 3, 4)
duration1.place(x=120, y=60)

tk.Label(mainWindow, text="Hours").place(x=205, y=60)
duration2=ttk.Combobox(mainWindow, width=10)
duration2['values'] = [i for i in range(0, 61)]
duration2.place(x=250, y=60)

tk.Label(mainWindow, text="Min").place(x=340, y=60)

tk.Label(mainWindow, text="Release Year").place(x=30, y=90)
release = ttk.Combobox(mainWindow, width=47)
release['values'] = [i for i in range(2019, 1950, -1)]
release.place(x=120, y=90)

tk.Label(mainWindow, text='Genre').place(x=30, y=120)
genre = ttk.Combobox(mainWindow, width=47)
genre['values'] = (' Action', ' Romance', ' Thrill', ' Comedy', ' Animation', ' Crime',
                   ' Drama', ' Horror', ' Biography')
genre.place(x=120, y=120)

tk.Label(mainWindow, text='Rating').place(x=30, y=150)
rating = ttk.Combobox(mainWindow, width=47)
rating['values'] = (5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0)
# rating['values'] = ("*", "**", "***", "****", "*****"  )
rating.place(x=120, y=150 )


def clear():
    name.delete(0, tk.END)
    rating.delete(0, tk.END)
    genre.delete(0, tk.END)
    duration1.delete(0, tk.END)
    duration2.delete(0, tk.END)
    release.delete(0, tk.END)

def addMovieRecord():
    movie_name = name.get()
    movie_genre = genre.get()
    movie_release = release.get()
    movie_rating = rating.get()
    movie_dur1 = duration1.get()
    movie_dur2 = duration2.get()
    movie_duration = movie_dur1+" Hours  "+movie_dur2+" Min "

    try:
        if(len(name.get()) != 0):
            db.insert_into(movie_name, movie_genre, movie_release, movie_rating, movie_duration)
            messagebox.showinfo("Save", "Record Save Successfully")
            clear()
        else:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", " Movie Name should not be blank")  # to be  checked

def viewRecords():
    showWindow = tk.Toplevel()
    showWindow.title(" Show Records ")
    showWindow.geometry("650x300")
    showWindow.resizable(width=False, height=False)

    cursor = db.viewTableCursor()
    count = db.colCount()

    L1 = tk.Label(showWindow, text="MOVIE_ID").grid(row=0, column=0, pady=10, padx=20)
    L2 = tk.Label(showWindow, text="MOVIE_NAME").grid(row=0, column=1, pady=10, padx=20)
    L3 = tk.Label(showWindow, text="DURATION").grid(row=0, column=2, pady=10, padx=20)
    L4 = tk.Label(showWindow, text="RELEASE").grid(row=0, column=3, pady=10, padx=20)
    L5 = tk.Label(showWindow, text="RATING").grid(row=0, column=4, pady=10, padx=20)
    L6 = tk.Label(showWindow, text="GENRE").grid(row=0, column=5, pady=10, padx=20)
    i = 1
    for row in cursor:
        j = 0
        for j in range(6):
            tk.Label(showWindow, text=row[j]).grid(row=i, column=j)
            j = j + 1
        i = i + 1
r

def deleteRec():
    deleteWindow = tk.Toplevel()
    deleteWindow.title(" Delete Record  ")
    deleteWindow.geometry("500x200")
    deleteWindow.resizable(0, 0)

    tk.Label(deleteWindow, text="Enter the Record No.").place(x=30, y=30)
    record = tk.Entry(deleteWindow, width=20)
    record.place(x=140, y=30)

    def takeRecNo():
        record1 = int(record.get())
        deleteQuery = db.delRec(record1)
        if (deleteQuery == 1):
            deleteWindow.destroy()
            messagebox.showerror("Error", "Record Deleted successfully...")
        else:
            deleteWindow.destroy()
            messagebox.showerror("Error", "Record not found...")

    submit = tk.Button(deleteWindow, text="Delete", width=7, command=lambda: takeRecNo()).place(x=180, y=70)
    deleteWindow.mainloop()



savebtn = tk.Button(mainWindow, text="Save", bd=4, width=7, command=lambda: addMovieRecord()).place(x=110, y=190)
showbtn = tk.Button(mainWindow, text="Show", bd=4, width=7, command=lambda: viewRecords()).place(x=180, y=190)
delbtn = tk.Button(mainWindow, text='Delete', bd=4, width=7, command=lambda: deleteRec()).place(x=250, y=190)
restbtn = tk.Button(mainWindow, text="Reset", bd=4, width=7, command=lambda: clear()).place(x=320, y=190)
extbtn = tk.Button(mainWindow, text='Exit', bd=4, width=7, command=quit).place(x=390, y=190)
# extbtn = tk.Button(mainWindow, text='Exit', bd=4, width=7, command=lambda: mainWindow.destroy()).place(x=390, y=190)


mainWindow.mainloop()