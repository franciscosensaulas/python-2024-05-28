def exemplo_vetor_frutas():
    # Criando um vetor(lugar para armazenar vários dados)
    frutas = []
    # .append adiciona o elemento no final do vetor

     # Maçã é armazenado na primeira posição do vetor de frutas
    frutas.append("Maçã")# ["Maçã"]
    frutas.append("Goiaba") # ["Maçã", "Goiaba"]
    frutas.append("Tomate") # ["Maçã", "Goiaba", "Tomate"]
    frutas.append("Banana")

    # Alterar o valor armazenado na primeira posição
    frutas[0] = "Apple" # ["Apple", "Goiaba", "Tomate"]

    # Remover o valor Banana da posição 3
    frutas.remove("Banana")

    print("Frutas:")
    print(frutas[0])
    print(frutas[1])
    print(frutas[2])
    print(frutas)


exemplo_vetor_frutas()