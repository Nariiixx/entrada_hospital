import csv
def menu():
    print("Menu de Opções:")
    print("1 - Cadastrar Paciente")
    print("2 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    while opcao in [1, 2]:
        if opcao == 1:
            print("Você escolheu Cadastrar Paciente.")
            # Aqui você pode chamar a função de cadastro de paciente
            nome = input("digite o nome do paciente:")
            if len(nome) < 3:
                print("Nome inválido. O nome deve ter pelo menos 3 caracteres.")
                
            idade = int(input("digite a idade do paciente:",)) 
            if idade > 100 or idade < 1:
                print("Idade inválida. A idade deve ser menor que 100 anos.")

            cpf = input("digite o cpf do paciente:")
            if cpf < '00000000000' or cpf > '99999999999':
                print("CPF inválido. O CPF deve ter 11 dígitos numéricos.")
                
            sus = input("digite o numero do sus do paciente:")
            if sus < '000000000000000' or sus > '999999999999999':
                print("Número do SUS inválido. O número do SUS deve ter 15 dígitos numéricos.")

            print("Paciente cadastrado com sucesso!")
            
            # Abrir o arquivo em modo de adição (append)
            with open('pacientes.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nome, idade, cpf, sus])
            break
        elif opcao == 2:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            opcao = int(input("Escolha uma opção: "))
    return opcao




