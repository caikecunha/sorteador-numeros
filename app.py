# ---- Import ----
import tkinter as tk
from tkinter import messagebox
import random

# ---- Função gerador ----
def gerador():
    inicio = num_inicio.get()
    final = num_final.get()
    if not inicio or not final:
        messagebox.showinfo("Sorteador", "Verifique se todos os campos foram preenchidos.")
    else:
        try:
            inicio = int(inicio)
            final = int(final)
            if final <= inicio:
                messagebox.showinfo("Sorteador", "O número final não pode ser menor ou igual do que o número inicial.")
            elif final > 10000:
                messagebox.showinfo("Sorteador", "Não é possível sortear números acima de 10.000")
            else:
                numero_gerado = random.randint(inicio, final)
                resultado["text"] = numero_gerado
        except:
            messagebox.showinfo("Sorteador", "Verifique se você digitou valores válidos.")

# ---- Configuração da interface gráfica ----
janela = tk.Tk()
janela.title("Sorteador")
janela.geometry("300x270+400+150")
janela.resizable(False, False)

titulo_label = tk.Label(janela, text="Sorteador de Número", font=("Arial", 16))
titulo_label.place(x=45, y=10)

texto_label = tk.Label(janela, text="Sortear entre", font=("Arial", 12))
texto_label.place(x=23, y=60)
texto2_label = tk.Label(janela, text="e", font=("Arial", 12))
texto2_label.place(x=183, y=60)

num_inicio = tk.Entry(janela, width=9)
num_inicio.place(x=121, y=63)
num_final = tk.Entry(janela, width=9)
num_final.place(x=203, y=63)

botao = tk.Button(janela, text="Sortear", font=("Arial", 12), bg="yellow", command=gerador)
botao.place(x=120, y=100)

# ultimo_gerado_label = tk.Label(janela, text="", font=("Arial", 10))
# ultimo_gerado_label.place(x=80, y=140)

resultado = tk.Label(janela, text="", font=("Arial", 50))
resultado.place(x=103, y=160)

credito = tk.Label(janela, text="© 2023 Caike Cunha", font=("Arial", 10))
credito.place(x=5, y=245)

versao = tk.Label(janela, text="v1.0.0", font=("Arial", 10))
versao.place(x=250, y=245)

janela.mainloop()
