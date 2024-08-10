# Usando seus conhecimentos aprendidos em sala, realize uma interface de
# login utilizando a biblioteca Tkinter em Python. O objetivo é permitir 
# que o usuário faça login somente se a senha tiver mais de 6 dígitos e 
# se o e-mail contiver o caractere "@", ou seja, realizar uma tela de 
# login com restrições de e-mail e senha.


import tkinter as tk
from tkinter import messagebox

def validar_login():
    email = entry_email.get()
    senha = entry_senha.get()
    
    if "@" not in email:
        messagebox.showerror("Erro", "O e-mail deve conter '@'.")
    elif len(senha) <= 6:
        messagebox.showerror("Erro", "A senha deve ter mais de 6 caracteres.")
    else:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")
janela.resizable(False, False)

tk.Label(janela, text="E-mail:").pack(pady=10)
entry_email = tk.Entry(janela, font=14, width=30)
entry_email.pack()

tk.Label(janela, text="Senha:").pack(pady=10)
entry_senha = tk.Entry(janela, font=14, width=30, show='*')
entry_senha.pack()

tk.Button(janela, text="Login", command=validar_login).pack(pady=20)

janela.mainloop()
