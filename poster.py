#Basic web poster with python by Burak "paradass" Görez

import json
import requests
import tkinter as tk

class Poster:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Paradass Poster")
        self.window.geometry("330x550")

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
    
    def post(self):
        url = self.url_box.get()
        payload = json.loads(self.payload_box.get("0.1",tk.END))
        response = requests.post(url=url,json=payload)
        self.response_box.delete("1.0",tk.END)
        if response.status_code == 200:
            self.response_box.insert("1.0","\n"+response.text)
            self.response_box.insert("1.0","Success:")
        else:
            self.response_box.insert("1.0",response.text)


poster = Poster()