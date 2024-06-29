import tkinter as tk
from tkinter import messagebox
from datetime import date


def acertar_data():
    try:
        dia = (entry_dia.get())
        mes = (entry_mes.get())

        if len(dia) > 2 or len(mes) > 2:
            messagebox.showerror("ERRO", "Dia ou mês não podem ter mais de dois dígitos.")
            return

        dia = int(dia)
        mes = int(mes)

        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            messagebox.showerror("ERRO", "Por favor insira um dia ou mês válido.")
            return

        hoje = date.today()
        if dia == hoje.day and mes == hoje.month:
            messagebox.showinfo("Resultado", "Feliz aniversário!!!!"
                                             "Você está de aniversário hoje.")
        else:
            messagebox.showinfo("Resultado", "Você não está de aniversário hoje.")
    except ValueError:
        messagebox.showerror("ERRO", "Por favor insira valores válidos.")


# Criação da Janela Principal
root = tk.Tk()

root.title("Você está de aniversário?")

# Criação dos widgets

label_dia = tk.Label(root, text="Insira o dia de nascimento: ")
label_dia.pack(pady=10)

entry_dia = tk.Entry(root)
entry_dia.pack(pady=5)

label_mes = tk.Label(root, text="Insira o mês de nascimento: ")
label_mes.pack(pady=10)

entry_mes = tk.Entry(root)
entry_mes.pack(pady=5)

button_verificar = tk.Button(root, text='Verificar', command=acertar_data)
button_verificar.pack(pady=15)

root.mainloop()
