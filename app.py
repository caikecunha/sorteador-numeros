# ---- Import ----
import tkinter as tk
from tkinter import ttk
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

# Configuração da janela principal
janela = tk.Tk()
janela.title("Sorteador de Números")
janela.geometry("400x400")
janela.configure(bg="#f7f7f7")
janela.resizable(False, False)

# Título
titulo_label = tk.Label(janela, text="Sorteador de Números", font=("Arial Rounded MT Bold", 20), bg="#f7f7f7", fg="#333")
titulo_label.pack(pady=20)

# Frame para entrada de números
frame_entrada = tk.Frame(janela, bg="#f7f7f7")
frame_entrada.pack(pady=10)

texto_label = tk.Label(frame_entrada, text="Sortear entre", font=("Arial", 12), bg="#f7f7f7", fg="#555")
texto_label.grid(row=0, column=0, padx=10)

num_inicio = ttk.Entry(frame_entrada, width=10, font=("Arial", 12))
num_inicio.grid(row=0, column=1, padx=5)

texto2_label = tk.Label(frame_entrada, text="e", font=("Arial", 12), bg="#f7f7f7", fg="#555")
texto2_label.grid(row=0, column=2, padx=5)

num_final = ttk.Entry(frame_entrada, width=10, font=("Arial", 12))
num_final.grid(row=0, column=3, padx=5)

# Botão para sortear
def botao_hover_in(event):
    botao.config(bg="#4CAF50", fg="#fff")

def botao_hover_out(event):
    botao.config(bg="#fff", fg="#4CAF50")

botao = tk.Button(janela, text="Sortear", font=("Arial", 12, "bold"), bg="#fff", fg="#4CAF50", relief="flat", command=gerador)
botao.pack(pady=20)
botao.bind("<Enter>", botao_hover_in)
botao.bind("<Leave>", botao_hover_out)

# Resultado
resultado = tk.Label(janela, text="", font=("Arial Rounded MT Bold", 50), bg="#f7f7f7", fg="#333")
resultado.pack(pady=20)

# Créditos e versão
rodape_frame = tk.Frame(janela, bg="#f7f7f7")
rodape_frame.pack(side="bottom", fill="x", pady=10)

credito = tk.Label(rodape_frame, text="© 2023 Caike Cunha", font=("Arial", 10), bg="#f7f7f7", fg="#888")
credito.pack(side="left", padx=10)

versao = tk.Label(rodape_frame, text="v1.0.0", font=("Arial", 10), bg="#f7f7f7", fg="#888")
versao.pack(side="right", padx=10)

janela.mainloop()

