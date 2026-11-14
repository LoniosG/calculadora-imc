import tkinter as tk
from tkinter import messagebox


class CalculadoraIMC:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cálculo do IMC - Índice de Massa Corporal")
        self.janela.geometry("700x430")
        self.janela.resizable(False, False)
        self.janela.configure(bg="#eeeeee")

        titulo = tk.Label(
            janela,
            text="Cálculo do IMC - Índice de Massa Corporal",
            font=("Arial", 15, "bold"),
            bg="#dddddd",
            pady=12
        )
        titulo.pack(fill="x")

        principal = tk.Frame(janela, bg="#eeeeee", padx=18, pady=18)
        principal.pack(fill="both", expand=True)

        tk.Label(principal, text="Nome do Paciente:", bg="#eeeeee",
                 font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=8)
        self.nome = tk.Entry(principal, font=("Arial", 11), width=43)
        self.nome.grid(row=0, column=1, columnspan=2, sticky="ew", pady=8)

        tk.Label(principal, text="Endereço Completo:", bg="#eeeeee",
                 font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=8)
        self.endereco = tk.Entry(principal, font=("Arial", 11), width=43)
        self.endereco.grid(row=1, column=1, columnspan=2, sticky="ew", pady=8)

        tk.Label(principal, text="Altura (cm):", bg="#eeeeee",
                 font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=8)
        self.altura = tk.Entry(principal, font=("Arial", 11), width=18)
        self.altura.grid(row=2, column=1, sticky="ew", pady=8, padx=(0, 10))

        tk.Label(principal, text="Peso (Kg):", bg="#eeeeee",
                 font=("Arial", 11)).grid(row=3, column=0, sticky="w", pady=8)
        self.peso = tk.Entry(principal, font=("Arial", 11), width=18)
        self.peso.grid(row=3, column=1, sticky="ew", pady=8, padx=(0, 10))

        self.resultado = tk.Label(
            principal,
            text="Resultado",
            bg="white",
            relief="solid",
            bd=1,
            font=("Arial", 11),
            width=27,
            height=7,
            wraplength=240,
            justify="center"
        )
        self.resultado.grid(row=2, column=2, rowspan=2, padx=8, pady=5, sticky="nsew")

        botoes = tk.Frame(principal, bg="#eeeeee")
        botoes.grid(row=4, column=0, columnspan=3, pady=22)

        tk.Button(botoes, text="Calcular", width=13, command=self.calcular,
                  font=("Arial", 10)).pack(side="left", padx=5)
        tk.Button(botoes, text="Reiniciar", width=13, command=self.reiniciar,
                  font=("Arial", 10)).pack(side="left", padx=5)
        tk.Button(botoes, text="Sair", width=13, command=self.janela.destroy,
                  font=("Arial", 10)).pack(side="left", padx=35)

        principal.columnconfigure(1, weight=1)
        principal.columnconfigure(2, weight=1)

    def calcular(self):
        nome = self.nome.get().strip()
        endereco = self.endereco.get().strip()

        if not nome or not endereco:
            messagebox.showwarning("Atenção", "Preencha o nome e o endereço do paciente.")
            return

        try:
            altura_cm = float(self.altura.get().replace(",", "."))
            peso = float(self.peso.get().replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Informe a altura e o peso usando números.")
            return

        if altura_cm <= 0 or peso <= 0:
            messagebox.showerror("Erro", "A altura e o peso devem ser maiores que zero.")
            return

        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        elif imc < 35:
            classificacao = "Obesidade grau I"
        elif imc < 40:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III"

        texto = (
            f"Paciente: {nome}\\n"
            f"IMC: {imc:.2f}\\n"
            f"Classificação: {classificacao}"
        )
        self.resultado.config(text=texto)

    def reiniciar(self):
        self.nome.delete(0, tk.END)
        self.endereco.delete(0, tk.END)
        self.altura.delete(0, tk.END)
        self.peso.delete(0, tk.END)
        self.resultado.config(text="Resultado")


if __name__ == "__main__":
    janela = tk.Tk()
    app = CalculadoraIMC(janela)
    janela.mainloop()
