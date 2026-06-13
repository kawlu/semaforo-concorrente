# Semáforo Concorrente em Python

Projeto desenvolvido para a disciplina **Programação e Plataformas de Alto Desempenho**.

## Descrição

Este sistema simula dois semáforos em um cruzamento utilizando programação concorrente em Python.

O projeto utiliza:

* Multithreading
* Lock (`threading.Lock`)
* Memória compartilhada
* Controle de fluxo de veículos

O sistema possui 3 threads:

* 1 thread responsável pelo controle dos semáforos
* 2 threads responsáveis pelo fluxo de veículos em cada rua

## Funcionamento

Os semáforos iniciam em estados opostos:

* Enquanto um eixo está em verde, o outro permanece em vermelho
* O ciclo dos sinais segue:

```text
VERDE → AMARELO → VERMELHO
```

### Comportamento do fluxo de veículos

#### 🔴 Vermelho

* Os carros apenas chegam
* A fila pode acumular até 30 carros

#### 🟡 Amarelo

* Entram de 1 a 2 carros
* Parte dos veículos pode atravessar

#### 🟢 Verde

* Poucos carros chegam
* A maioria dos veículos atravessa

## Estruturas Compartilhadas

### Quantidade de carros

```python
qntd_carro = {
    "rua_y": 0,
    "rua_x": 0
}
```

### Estado dos semáforos

```python
sinal = {
    "y": "VERDE",
    "x": "VERMELHO"
}
```

## Execução

Execute o arquivo principal com:

```bash
python main.py
```

## Tecnologias Utilizadas

* Python 3
* threading
* time
* random
