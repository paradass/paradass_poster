#Basic web poster with python by Burak "paradass" Görez

import json
import requests
import tkinter as tk
from tkinter import messagebox

class Poster:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Paradass Poster")
        self.window.geometry("330x550")
        icon = tk.PhotoImage(file="icon.png")
        self.window.iconphoto(True,icon)

        self.label1 = tk.Label(self.window,text="Target url:",font=("Arial",12))
        self.label1.place(x=10,y=10)

        self.url_box = tk.Entry(self.window,font=("Arial",12))
        self.url_box.place(x=10,y=40,width=300)

        self.label2 = tk.Label(self.window,text="Json payload:",font=("Arial",12))
        self.label2.place(x=10,y=90)

        self.payload_box = tk.Text(self.window,font=("Arial",12))
        self.payload_box.place(x=10,y=120,width=300,height=100)

        self.button = tk.Button(self.window,text="Post",command=self.post,font=("Arial",12))
        self.button.place(x=10,y=250)

        self.label3 = tk.Label(self.window,text="Response:",font=("Arial",12))
        self.label3.place(x=10,y=300)

        self.response_box = tk.Text(self.window,font=("Arial",12))
        self.response_box.place(x=10,y=330,width=300,height=200)

        self.window.mainloop()
    
    @staticmethod
    def show_error(e:Exception):
        messagebox.showerror("Error",str(e))

    def post(self):
        try:
            url = self.url_box.get()
            payload = json.loads(self.payload_box.get("1.0",tk.END))
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
            response = requests.post(url=url,json=payload,headers=headers,timeout=10)
            self.response_box.delete("1.0",tk.END)

            if response.ok:
                self.response_box.insert("1.0","\n"+response.text)
                self.response_box.insert("1.0","Success:")
            else:
                self.response_box.insert("1.0","\n"+response.text)
                self.response_box.insert("1.0","Fail:")
        except Exception as e:
            self.show_error(e)
            return

poster = Poster()