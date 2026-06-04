# Trabalho-OAC-LOGICA
Projeto de um simulador de hardware (UCP/RAM) e escalonador de processos desenvolvido em Python para a avaliação AV2.



# Simulador de Computador - AV2

## Sobre o Projeto
Este projeto foi desenvolvido como parte da avaliação **AV2** da disciplina de **Organização e Arquitetura de Computadores** integrada com **Lógica de Programação**. 


---

## Integrantes : 
Gabriel Buarque, 
Vinicius Guerra, 
Rai Henrique.


---

O objetivo principal é construir um **Simulador de Computador** funcional em Python que demonstre visualmente, através do console, como o hardware (Processador e Memória RAM) e o Sistema Operacional (Escalonador de Processos) interagem para executar instruções e alternar tarefas.

---

## Arquitetura do Simulador

O simulador foi dividido em 4 pilares fundamentais de um sistema computacional real:

### 1. O Hardware Virtual
* **Memória RAM:** Representada por um vetor (lista) de 6 posições, onde os programas são carregados sequencialmente.
* **Processador (UCP):** Representado por um dicionário contendo dois registradores de uso geral: `R1` e `R2`.

### 2. O Conjunto de Instruções
O processador foi ensinado a interpretar e executar comandos em "linguagem de montagem" (Assembly):
* `MOVER [Registrador] [Valor]`: Atribui um valor inteiro a um registrador.
* `SOMAR [Registrador] [Valor]`: Soma um valor ao conteúdo atual do registrador.
* `SUBTRAIR [Registrador] [Valor]`: Subtrai um valor do conteúdo atual do registrador.
* `FIM`: Sinaliza o término da execução daquele programa.

### 3. O Cérebro (Loop de Execução)
O simulador utiliza um loop contínuo (`while True`) que realiza o ciclo tradicional de um processador:
1. **Busca** a instrução na memória RAM utilizando o ponteiro correspondente.
2. **Decodifica** a instrução separando os comandos e argumentos.
3. **Executa** a operação diretamente nos registradores do processador.

### 4. O Sistema Operacional (Escalonador)
Para simular a multiprogramação (vários programas rodando "ao mesmo tempo"), foi implementada uma lógica de **Escalonamento Alternado**. O laço de repetição executa uma instrução do **Programa 1** e, logo em seguida, uma instrução do **Programa 2**, revezando o uso do processador de forma justa até que ambos cheguem ao comando `FIM`.






## Como Executar o Simulador

### Pré-requisitos
* Ter o **Python 3.x** instalado em sua máquina.




### Passo a Passo
1. Abra o terminal na pasta do projeto.
2. Execute o comando correspondente ao arquivo do seu código:

```bash
python main.py