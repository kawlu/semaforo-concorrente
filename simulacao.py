import threading
import time
import random

# Memória compartilhada
qntd_carro = {"rua_y": 0, "rua_x": 0}

sinal = {"y": "VERDE", "x": "VERMELHO"}

# Instância de lock
lock = threading.Lock()


# Configuração
TEMPO_VERDE = 5
TEMPO_AMARELO = 2
TEMPO_LOOP = 1
LIMITE_CARROS = 30


# Função que controla a cor dos dois semáforos
def controlador_de_semaforos():

    while True:

        time.sleep(TEMPO_VERDE)

        with lock:
            sinal["y"] = "AMARELO"

        time.sleep(TEMPO_AMARELO)

        with lock:
            sinal["y"] = "VERMELHO"
            sinal["x"] = "VERDE"

        time.sleep(TEMPO_VERDE)

        with lock:
            sinal["x"] = "AMARELO"

        time.sleep(TEMPO_AMARELO)

        with lock:
            sinal["x"] = "VERMELHO"
            sinal["y"] = "VERDE"


# Função que gere o fluxo de veículos (saídas | entradas) de acordo com a cor do semafóro
def fluxo_veiculos(rua, eixo):

    while True:

        with lock:

            # Estado inicial
            estado = sinal[eixo]

            if estado == "VERDE":
                chegando = random.randint(0, 3)

                # Atualiza e respeita o limite máximo de carros da via
                qntd_carro[rua] = min(LIMITE_CARROS, qntd_carro[rua] + chegando)

                if qntd_carro[rua] > 0:

                    maior_int = min(5, qntd_carro[rua])
                    menor_int = max(1, min(qntd_carro[rua] // 2, maior_int))

                    saindo = random.randint(menor_int, maior_int)

                    qntd_carro[rua] -= saindo

            elif estado == "AMARELO":
                chegando = random.randint(1, 2)

                # Atualiza e respeita o limite máximo de carros da via
                qntd_carro[rua] = min(LIMITE_CARROS, qntd_carro[rua] + chegando)

                atravessar = random.choice([True, False])

                if atravessar and qntd_carro[rua] > 0:
                    saindo = max(1, qntd_carro[rua] // 3)
                    qntd_carro[rua] -= saindo

            # VERMELHO
            else:
                chegando = random.randint(2, 4)
                qntd_carro[rua] = min(LIMITE_CARROS, qntd_carro[rua] + chegando)

        time.sleep(TEMPO_LOOP)


# =========================
# Inicialização
# =========================


def iniciar_threads():

    t_controlador = threading.Thread(target=controlador_de_semaforos, daemon=True)

    t_y = threading.Thread(target=fluxo_veiculos, args=("rua_y", "y"), daemon=True)

    t_x = threading.Thread(target=fluxo_veiculos, args=("rua_x", "x"), daemon=True)

    t_controlador.start()
    t_y.start()
    t_x.start()
