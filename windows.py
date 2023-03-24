from tkinter import *
from tkinter import messagebox
import webbrowser
import openai
import requests

class GPT(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.check_internet_connection()
        

    def check_internet_connection(self):
        try:
            requests.get('https://google.com')
            self.Login()
            return True
        except requests.ConnectionError:
            messagebox.showerror(message='Sin internet',title="Connection")
            return False 

    def userLogin(self):
        def on_enter_user(e):
            self.user.delete(0,'end')

        def on_leave_user(e):
            name = self.user.get()
            if name =='':
                self.user.insert(0,'Username')
        self.user = Entry(self.fm,width=25,border=0,bg='#1E2227',fg='white',font=('Microsoft YaHei UI Light',15))
        self.user.place(x=10,y=50)
        self.user.insert(0,'Username')
        Frame(self.fm,width=280,height=2,bg='white').place(x=10,y=80)
        self.user.bind('<FocusIn>',on_enter_user)
        self.user.bind('<FocusOut>',on_leave_user)

    def keyGPT(self):
        def on_enter_key(e):
            self.key.delete(0,'end')

        def on_leave_key(e):
            name = self.key.get()
            if name =='':
                self.key.insert(0,'API keys')
                
        self.key = Entry(self.fm,width=25,border=0,bg='#1E2227',fg='white',font=('Microsoft YaHei UI Light',15))
        self.key.place(x=10,y=110)
        self.key.insert(0,'Key de OpenAI')
        Frame(self.fm,width=280,height=2,bg='white').place(x=10,y=140)
        self.key.bind('<FocusIn>',on_enter_key)
        self.key.bind('<FocusOut>',on_leave_key)

    def singIn(self):
        def open_url():
            url = "https://platform.openai.com/account/api-keys"
            webbrowser.open_new(url)

        Label(self.fm,text="Don't have an account",fg='white',bg='#1E2227',font=('Microsoft YaHei UI Light',9)).place(x=40,y=270)
        singInBtn = Button(self.fm,cursor='hand2',text='Sign In',fg='#5DADE2',bg='#1E2227',border=0,font=('Microsoft YaHei UI Light',9),command=open_url)
        singInBtn.place(x=180,y=270)

    def bhoran(self):

        def Api_ChatGPT(text):
            try:
                openai.api_key =f'{self.key.get()}'
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=text,
                    max_tokens=2048,
                    temperature=0.9,
                )
                message = response.choices[0].text.strip()
                return message
            except Exception as e:
                return f"Error: {e}"

        def conversation():
            text = self.prompt.get('1.0',END)
            user = self.user.get()
            self.txt.config(state='normal')
            self.txt.insert(END,f'{user}:\n{text}\n\n')
            self.prompt.delete('1.0',END)

            response = Api_ChatGPT(text)
            self.txt.insert(END,f'Bhoran:\n{response}\n\n\n')
            self.txt.config(state='disabled')

        self.master.wm_title('Bhoran')
        frame = Frame(self.master,width=400,height=700,bg='#1E2227')
        frame.place(x=0)
        Frame(frame,width=380,height=2,bg='white').place(x=10,y=590)

        frame1 = Frame(frame,width=400,height=580)
        frame1.place(x=7,y=5)

        self.txt = Text(frame1,width=41,height=32,border=0,bg='#1E2227',fg='white',font=(12))
        sb = Scrollbar(frame1,orient=VERTICAL)
        sb.pack(side=RIGHT,fill=Y)
        self.txt.pack(side=LEFT, fill = Y)
        self.txt.config(yscrollcommand=sb.set)
        sb.config(command=self.txt.yview)
        self.txt.config(state='disabled')


        frame2 = Frame(frame,width=400,height=100,bg='#1E2227')
        frame2.place(x=0,y=595)
        self.prompt = Text(frame2,width=34,height=5,border=0,bg='#40414F',fg='white',font=(12))
        self.prompt.place(x=7,y=5)
        


        self.btnPrompt = Button(frame2,text='Enviar',bg='#40414F',fg='white',border=0,cursor='hand2',font=20)
        self.btnPrompt.config(width=7,height=4, command=conversation)
        self.btnPrompt.place(x=322,y=10)
        
    def Login(self):

        def newFrame():
            self.bhoran()

        Label(self.master, text='Chat Bot',fg='white',bg='#1E2227',font=('Microsoft YaHei UI Light',25,'bold')).place(x=135,y=20) 
        Label(self.master, text='Bot creado con la API de GPT-3',fg='white',bg='#1E2227',font=('Microsoft YaHei UI Light',12,'bold')).place(x=70,y=350)
        self.fm = Frame(self.master,width=300,height=300,bg='#1E2227')
        self.fm.place(x=60,y=380)
        
        self.userLogin()
        self.keyGPT()

        btn = Button(self.fm,width=20,pady=7,text='Sign In',fg='#5DADE2',bg='white',border=0,font=('Lucida Grande',18),command=newFrame)
        btn.place(x=10,y=175)
        self.singIn()