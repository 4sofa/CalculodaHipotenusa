import tkinter as tk
from tkinter import messagebox


def converter():
    try:
        catajacente = float(entry_catajacente.get())
        catoposto = float(entry_catoposto.get())

        if catajacente <= 0 or catoposto <= 0:
            messagebox.showerror('Erro', 'Os valores devem ser positivos')
            return

        hipotenusa = ((catajacente ** 2) + (catoposto ** 2)) ** 0.5
        label_result.config(text=f"Resultado hipotenusa: {hipotenusa:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")


# Criação da janela principal

root = tk.Tk()

root.title("Calculo da Hipotenusa")

# Criação dos widgets
label_catajacente = tk.Label(root, text="Insira a base: ")
label_catajacente.pack(pady=10)

entry_catajacente = tk.Entry(root)
entry_catajacente.pack(pady=5)

label_catoposto = tk.Label(root, text="Insira a Altura: ")
label_catoposto.pack(pady=10)

entry_catoposto = tk.Entry(root)
entry_catoposto.pack(pady=5)

button_convert = tk.Button(root, text="Calcular", command=converter)
button_convert.pack(pady=10)

label_result = tk.Label(root, text="Resultado: ")
label_result.pack(pady=20)

# Execução da interface
root.mainloop()
