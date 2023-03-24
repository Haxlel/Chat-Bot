from tkinter import *
from windows import GPT

def main ():
    root = Tk()
    root.wm_title('Login')
    root.geometry('400x700+300+200')
    root.configure(bg='#1E2227', border=0)
    root.iconbitmap('.\\bot.ico')
    root.resizable(False,False)
    
    img = PhotoImage(file='.\\bot.png')
    Label(root,image=img,bg='#1E2227').place(x=100,y=80)

    app = GPT(root)
    app.mainloop()


if __name__ =="__main__":
    main()