import tkinter as tk

def converte():
    cm = float(entry_cm.get())
    label_result.config(text=f'{cm / 100:.2f} metros')


# Configurações da tela
janela = tk.Tk()
janela.title("Converter de cm para metros")
janela.geometry("300x300")
janela.resizable(False, False)

# Configurações label - entrada
tk.Label(janela, text="Insira o valor em centímetros:").pack()
entry_cm = tk.Entry(janela, font=14, width=20)
entry_cm.pack()

# Configuraçẽos botão
tk.Button(janela, text="Converter", command=converte).pack()

# Resultado da conversão
label_result = tk.Label(janela, text="", font=14)
label_result.pack()

# Iniciar interface gráfica
janela.mainloop()
