import tkinter as tk

from simulacao import qntd_carro, sinal, lock

largura = 700
altura = 400

janela = tk.Tk()

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

pos_y = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)

janela.title("Controle de Semáforo Inteligente")
janela.geometry(f"{largura}x{altura}+{pos_y}+{pos_y}")
janela.config(bg="white")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="Simulação Concorrente de Trânsito",
    font=("Arial", 18, "bold"),
    bg="white",
)

titulo.pack(pady=20)

frame = tk.Frame(janela, bg="white")
frame.pack()


# Eixo Y
frame_y = tk.Frame(frame, bg="white", padx=40)
frame_y.grid(row=0, column=0)

tk.Label(frame_y, text="Norte-Sul", font=("Arial", 16, "bold"), bg="white").pack()

canvas_y = tk.Canvas(frame_y, width=100, height=220, bg="black")

canvas_y.pack(pady=10)

luz_vermelha_y = canvas_y.create_oval(25, 20, 75, 70, fill="gray")

luz_amarela_y = canvas_y.create_oval(25, 85, 75, 135, fill="gray")

luz_verde_y = canvas_y.create_oval(25, 150, 75, 200, fill="gray")

label_rua_y = tk.Label(frame_y, text="Carros: 0", font=("Arial", 14), bg="white")

label_rua_y.pack(pady=10)


# Eixo X

frame_x = tk.Frame(frame, bg="white", padx=40)
frame_x.grid(row=0, column=1)

tk.Label(frame_x, text="Leste-Oeste", font=("Arial", 16, "bold"), bg="white").pack()

canvas_x = tk.Canvas(frame_x, width=100, height=220, bg="black")

canvas_x.pack(pady=10)

luz_vermelha_x = canvas_x.create_oval(25, 20, 75, 70, fill="gray")

luz_amarela_x = canvas_x.create_oval(25, 85, 75, 135, fill="gray")

luz_verde_x = canvas_x.create_oval(25, 150, 75, 200, fill="gray")

label_rua_x = tk.Label(frame_x, text="Carros: 0", font=("Arial", 14), bg="white")

label_rua_x.pack(pady=10)

# =========================
# Atualização visual
# =========================


def atualizar_interface():

    with lock:

        estado_y = sinal["y"]
        estado_x = sinal["x"]

        rua_y = qntd_carro["rua_y"]
        rua_x = qntd_carro["rua_x"]

    # Reset
    for canvas, vermelho, amarelo, verde in [
        (canvas_y, luz_vermelha_y, luz_amarela_y, luz_verde_y),
        (canvas_x, luz_vermelha_x, luz_amarela_x, luz_verde_x),
    ]:

        canvas.itemconfig(vermelho, fill="gray")
        canvas.itemconfig(amarelo, fill="gray")
        canvas.itemconfig(verde, fill="gray")

    # Eixo Y
    if estado_y == "VERDE":
        canvas_y.itemconfig(luz_verde_y, fill="green")

    elif estado_y == "AMARELO":
        canvas_y.itemconfig(luz_amarela_y, fill="yellow")

    else:
        canvas_y.itemconfig(luz_vermelha_y, fill="red")

    # Eixo X
    if estado_x == "VERDE":
        canvas_x.itemconfig(luz_verde_x, fill="green")

    elif estado_x == "AMARELO":
        canvas_x.itemconfig(luz_amarela_x, fill="yellow")

    else:
        canvas_x.itemconfig(luz_vermelha_x, fill="red")

    # Contadores
    label_rua_y.config(text=f"Carros: {rua_y}")

    label_rua_x.config(text=f"Carros: {rua_x}")

    janela.after(200, atualizar_interface)


def iniciar_interface():

    atualizar_interface()
    janela.mainloop()
