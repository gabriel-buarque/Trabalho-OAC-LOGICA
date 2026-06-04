import time

# O Hardware Virtual
ram = [""] * 6
processador = {"R1": 0, "R2": 0}

# Gravando o Programa 1 na RAM
ram[0] = "MOVER R1 10"
ram[1] = "SOMAR R1 5"
ram[2] = "FIM"

# Gravando o Programa 2 na RAM
ram[3] = "MOVER R2 20"
ram[4] = "SUBTRAIR R2 2"
ram[5] = "FIM"

# Variáveis para saber em qual linha cada programa está (Program Counters)
linha_p1 = 0
linha_p2 = 3

print("Iniciando o Simulador de Computador...\n")

# Loop e sistema operacional (Escalonador)
while True:
    instrucao1 = ram[linha_p1]
    instrucao2 = ram[linha_p2]

    # Condição de parada de ambos os programas
    if instrucao1 == "FIM" and instrucao2 == "FIM":
        print("\nTodos os programas terminaram com sucesso!")
        print("Valores finais no processador:", processador)
        break

    # Execução do Programa 1
    if instrucao1 != "FIM":
        print(f"Programa 1 executando: {instrucao1}")
        
        partes = instrucao1.split() 
        if partes[0] == "MOVER": 
            processador[partes[1]] = int(partes[2])
        elif partes[0] == "SOMAR": 
            processador[partes[1]] += int(partes[2])
        
        linha_p1 += 1 
    
    # Execução do Programa 2
    if instrucao2 != "FIM":  
        print(f"Programa 2 executando: {instrucao2}")
        
        time.sleep(1) 

        partes = instrucao2.split()
        if partes[0] == "MOVER": 
            processador[partes[1]] = int(partes[2])
        elif partes[0] == "SUBTRAIR": 
            processador[partes[1]] -= int(partes[2])
        
        linha_p2 += 1  

    print(f"Estado atual do Processador: {processador}")
    print("-" * 40)
    time.sleep(0.5)