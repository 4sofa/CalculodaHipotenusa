import tkinter as tk
from tkinter import messagebox


def converter():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        cateto = ((base ** 2) + (altura ** 2))
        c3 = cateto ** 0.5
        label_result.config(text=f"{c3:.2f} cateto3")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")


# Criação da janela principal
root = tk.Tk()
root.title("Calculo do Triangulo")

# Criação dos widgets
label_base = tk.Label(root, text="Insira a base abaixo:")
label_base.pack(pady=10)

entry_base = tk.Entry(root)
entry_base.pack(pady=5)

label_altura = tk.Label(root, text="Insira a Altura abaixo")
label_altura.pack(pady=10)

entry_altura = tk.Entry(root)
entry_altura.pack(pady=5)

button_convert = tk.Button(root, text="Calcular", command=converter)
button_convert.pack(pady=10)

label_result = tk.Label(root, text="Resultado: ")
label_result.pack(pady=20)

# Execução da interface
root.mainloop()
