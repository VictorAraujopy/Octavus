import tkinter as tk
from PIL import Image, ImageTk
import subprocess

processo = None  # armazena o processo do main.py

def ao_clicar():
    global processo
    if processo is None:
        texto.config(text="Octavus listening... wait a sec")
        processo = subprocess.Popen(['pythonw', 'main.py'])  # inicia Octavus
    else:
        texto.config(text="Octavus stopped listening.")
        processo.terminate()  # para o main.py
        processo = None

# Interface
janela = tk.Tk()
janela.title("Octavus Interface")
janela.geometry("300x500")
janela.configure(bg='#0A1B2A')

imagem = Image.open(r"imagens\octavus.png")
imagem = imagem.resize((120, 150))
img = ImageTk.PhotoImage(imagem)
label_img = tk.Label(janela, image=img, bg='#0A1B2A')
label_img.pack(pady=40)

texto = tk.Label(janela, text="Tap the microphone to begin", fg='white', bg='#0A1B2A', font=("Helvetica", 12))
texto.pack()

microfone_img = Image.open(r"imagens\microfone.png")
microfone_img = microfone_img.resize((90, 120))
microfone = ImageTk.PhotoImage(microfone_img)

botao = tk.Button(janela, image=microfone, command=ao_clicar, bg='#0A1B2A', bd=0, activebackground='#0A1B2A')
botao.pack(pady=20)

janela.mainloop()
