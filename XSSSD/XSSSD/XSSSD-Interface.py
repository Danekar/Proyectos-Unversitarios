import XSSSD
import asyncio
import tkinter as tk
from tkinter import *
import sys

#sys.setrecursionlimit(10000)

class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()

class Window(Tk):
    def __init__(self, loop):
        
        self.loop = loop
        self.root = Tk()
        self.root.configure(bg=self.Colors.black)
        self.SetUrlEntryText = tk.StringVar()
        self.SetInputEntryText = tk.StringVar()
        

        self.IntroUrlLabel = tk.Label(text="Introduce URL: ",bg=self.Colors.blue, fg=self.Colors.green,width=30).grid(column=0,row=0)
        self.IntroInputLabel = tk.Label(text="Introduce Input: ",bg=self.Colors.blue, fg=self.Colors.green,width=30).grid(column=0,row=1)
        self.SetUrlEntry = tk.Entry(width=50, textvariable=self.SetUrlEntryText,bg=self.Colors.blue, fg=self.Colors.green).grid(column=1,row=0)
        self.SetInputEntry = tk.Entry(width=50, textvariable=self.SetInputEntryText,bg=self.Colors.blue, fg=self.Colors.green).grid(column=1,row=1)
        self.SearchButton = tk.Button(text="Exploit",width=10,height=5,command=self.exploit,bg=self.Colors.blue, fg=self.Colors.green).grid(column=2,row=0,columnspan=2,rowspan=2, pady=10)
        self.SearchButton = tk.Button(text="Save",width=10,height=5,command=self.saveInDisc,bg=self.Colors.blue, fg=self.Colors.green).grid(column=2,row=2,padx=10)
        self.VulenrableUrlListbox = tk.Listbox(width=40, bg=self.Colors.blue, fg=self.Colors.green)
        self.VulenrableUrlListbox.grid(column=0,row=2,padx=10)
        self.VulenrabilitiesPerUrl = tk.Text(bg=self.Colors.blue, fg=self.Colors.green,state="disabled")
        self.VulenrabilitiesPerUrl.grid(column=1,row=2, pady=10)
        self.VulenrableUrlListbox.bind("<<ListboxSelect>>", self.pepe)
        
        self.arrayOfVulnerabilities = {}
        self.saves=0
        
    async def show(self):
        while True:
            try:
                self.root.state()
                self.root.update()
                await asyncio.sleep(.1)
            except:
                break
    
    class Colors():
        black = "#000033"
        blue = "#3137fd"
        green="#66ff33"

    
    #payloadsValidos = XSSSD.payloadsValidos
    
    def pepe(self,event):
       asyncio.gather(self.vulnerabilitiesText(event))
    
    async def vulnerabilitiesText(self,event):
        try:
            ListaVulnSinCorchetes = self.arrayOfVulnerabilities[self.VulenrableUrlListbox.get(self.VulenrableUrlListbox.curselection()[0])]
            self.VulenrabilitiesPerUrl.config(state="normal")
            self.VulenrabilitiesPerUrl.delete('1.0', END)
            self.VulenrabilitiesPerUrl.insert(INSERT, "\n ------------------------------Estos payloads servirían---------------------- \n")
            #ListaVulnSinCorchetes = arrayOfVulnerabilities[event.widget.get(event.widget.curselection())]
            self.VulenrabilitiesPerUrl.insert(INSERT,"\n")
            for payloads in ListaVulnSinCorchetes:
                self.VulenrabilitiesPerUrl.insert(INSERT,payloads)
                self.VulenrabilitiesPerUrl.insert(INSERT,"\n")
                self.VulenrabilitiesPerUrl.insert(INSERT,"\n")
            self.VulenrabilitiesPerUrl.config(state="disabled")
        except:
            print
        
    async def ponerNombre(self):
        await asyncio.sleep(1)
        self.VulenrableUrlListbox.insert(tk.END,XSSSD.urlLink)
        await asyncio.sleep(1)
        self.arrayOfVulnerabilities[XSSSD.urlLink] = XSSSD.payloadsValidos

    async def executeOrder66(self):
        XSSSD.urlLink = self.SetUrlEntryText.get()
        XSSSD.inputLink = self.SetInputEntryText.get()
        XSSSD.payloadsValidos=[]
        XSSSD.posicionRespuesta=0
        XSSSD.respuesta=""
        asyncio.gather(XSSSD.main())
        asyncio.gather(self.ponerNombre())
        
    def exploit(self):
        asyncio.gather(self.executeOrder66())   
        
    def saveInDisc(self):
        self.saves+=1
        with open('SavedOutputs/output'+str(self.saves)+'.txt', 'w') as f:
            for key in self.arrayOfVulnerabilities:
                f.write(str(key) + ': ' + str(self.arrayOfVulnerabilities[key]) + '\n\n')
        

    



asyncio.run(App().exec())