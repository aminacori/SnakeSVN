from tkinter import *
from tkinter import filedialog


def browseFiles():
    filename = filedialog.askopenfilename(initialdir='/', title='Seleziona un file',
                                          filetypes=(("File di testo", ".txt"), ("Tutti", "*.*")))
    label_file_explorer.configure(text="File Opened: " + filename)


window = Tk()
window.title("File Explorer")
window.geometry("500x500")
window.config(background="gray")
label_file_explorer = Label(window, text="File Explore che usa TkInter", fg="blue", width=100, height=4)
button_explore = Button(window, text="Naviga file...", command=browseFiles)
button_exit = Button(window, text="Esci", command=exit)
label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2)
button_exit.grid(column=1, row=3)

window.mainloop()
