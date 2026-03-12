"""Aplicação de consola para gerar utentes e verificar interações.

O programa mantém uma lista de utentes gerados aleatoriamente e uma matriz
simulada de interações entre medicamentos lidos de um ficheiro. O utilizador
pode:

1. Gerar números de utentes
2. Atribuir medicamentos a um utente
3. Listar utentes
4. Mostrar a matriz de interações
5. Avaliar combinações de medicamentos de um utente
6. Exportar utentes para JSON/CSV
7. Sair
"""

import generateNumeroUtente 
import generateReceita
from combinationMatrix import gerar_matriz_combinacao, buscar_interacao
from itertools import combinations
import json
import csv

def main():
    """Função principal que exibe um menu e processa as opções do utilizador.

    Ao começar, gera a matriz de combinações de medicamentos a partir do
    ficheiro `medicamentos.txt`. Mantém `lista_numeros` com os utentes criados.
    O loop principal solicita ao utilizador uma opção, executa a ação e repete
    até que seja escolhida a saída.
    """
    # gerar matriz de combinações no início
    medicamentos, matriz_combinacoes = gerar_matriz_combinacao()

    lista_numeros = []

    while True:
        print(r"""   _____                     /\/|             _                          _ _            
  / ____|                   |/\/             | |                        (_) |           
 | |  __  ___ _ __ __ _  ___ __ _  ___     __| | ___   _ __ ___  ___ ___ _| |_ __ _ ___ 
 | | |_ |/ _ \ '__/ _` |/ __/ _` |/ _ \   / _` |/ _ \ | '__/ _ \/ __/ _ \ | __/ _` / __|
 | |__| |  __/ | | (_| | (_| (_| | (_) | | (_| |  __/ | | |  __/ (_|  __/ | || (_| \__ \
  \_____|\___|_|  \__,_|\___\__,_|\___/   \__,_|\___| |_|  \___|\___\___|_|\__\__,_|___/
                         )_)                                                            
                                                                                        """)
        print("1. Generar numero de utentes")
        print("2. Gerar lista de medicamentos para o utente")
        print("3. Mostrar lista de utentes")
        print("4. Mostrar matriz de combinações de medicamentos")
        print("5. Buscar combinações de medicamentos de um utente")
        print("6. Importar utentes para CSV")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
    

        match opcao:
            case "1":
                print("Escolha o numero de utentes a gerar: ")
                try:
                    numero_de_utentes = int(input("Número de utentes: "))
                    lista_numeros = generateNumeroUtente.gerar_numero_utente(numero_de_utentes)
                    print(lista_numeros)
                except ValueError:
                    print("Entrada inválida! Por favor, insira um número inteiro.")
            case "2":
                if not lista_numeros:
                    print("Erro: Nenhum utente foi gerado. Primeiro, execute a opção 1.")
                else:
                    print("Escolha o número do utente: ")
                    try:
                        numero_utente = str(input("Número do utente: "))
                        
                        # Procurar o utente na lista
                        utente_encontrado = None
                        for utente in lista_numeros:
                            if utente["numero_utente"] == numero_utente:
                                utente_encontrado = utente
                                break
                        
                        if utente_encontrado is None:
                            print(f"Utente com número {numero_utente} não encontrado!")
                        else:
                            print("Escolha o numero de medicamentos para a receita (entre 3-5): ")
                            numero_de_medicamentos = int(input("Número de medicamentos: "))
                            if 3 <= numero_de_medicamentos <= 5:
                                lista_medicamentos = generateReceita.gerar_lista_medicamentos(numero_de_medicamentos)
                                utente_encontrado["medicamentos"] = lista_medicamentos
                                print(f"Medicamentos adicionados ao utente {utente_encontrado['nome']}:")
                            else:
                                print("Número inválido! Por favor, escolha entre 3 e 5.")
                    except ValueError:
                        print("Entrada inválida! Por favor, insira um número inteiro.")
                    
            case "3":
                if not lista_numeros:
                    print("Nenhum utente foi gerado ainda.")
                else:
                    print("\n=== Lista de Utentes ===")
                    for utente in lista_numeros:
                        print(utente)
                    print()
                
            case "4":
                # mostrar apenas os ratings da matriz de combinações
                if not medicamentos or not matriz_combinacoes:
                    print("Matriz de combinações não gerada.")
                else:
                    for linha in matriz_combinacoes:
                        print(" ".join(str(v) for v in linha))
            case "5":
                # buscar combinações de medicamentos do utente
                if not lista_numeros:
                    print("Erro: Nenhum utente foi gerado. Primeiro, execute a opção 1.")
                else:
                    print("Escolha o número do utente: ")
                    try:
                        numero_utente = str(input("Número do utente: "))
                        
                        # Procurar o utente na lista
                        utente_encontrado = None
                        for utente in lista_numeros:
                            if utente["numero_utente"] == numero_utente:
                                utente_encontrado = utente
                                break
                        
                        if utente_encontrado is None:
                            print(f"Utente com número {numero_utente} não encontrado!")
                        elif "medicamentos" not in utente_encontrado:
                            print(f"Utente {utente_encontrado['nome']} não possui medicamentos atribuídos!")
                        else:
                            # gerar combinações de 2 medicamentos
                            meds = utente_encontrado["medicamentos"]
                            combos = list(combinations(meds, 2))
                            
                            if not combos:
                                print("Não há combinações possíveis com menos de 2 medicamentos.")
                            else:
                                print(f"\n=== Interações de medicamentos para {utente_encontrado['nome']} ===")
                                ratings = []
                                for med1, med2 in combos:
                                    rating = buscar_interacao(medicamentos, matriz_combinacoes, med1, med2)
                                    if rating is not None:
                                        print(f"{med1} + {med2}: {rating}")
                                        ratings.append(rating)
                                    else:
                                        print(f"{med1} + {med2}: Medicamento não encontrado")
                                
                                # verificar se passou ou não passou
                                if any(r > 0 for r in ratings):
                                    print("\n>>> NÃO PASSOU <<<")
                                else:
                                    print("\n>>> PASSOU <<<")
                                print()
                    except ValueError:
                        print("Entrada inválida! Por favor, insira um número inteiro.")
            case "6":
                try:
                    json_str = json.dumps(lista_numeros, ensure_ascii=False, indent=2)
                    with open('utentes.json', 'w', encoding='utf-8') as jf:
                        jf.write(json_str)
                    print("Arquivo utentes.json criado.")

                    # converter json para csv
                    if lista_numeros:
                        keys = lista_numeros[0].keys()
                        with open('utentes.csv', 'w', newline='', encoding='utf-8') as cf:
                            writer = csv.DictWriter(cf, fieldnames=keys)
                            writer.writeheader()
                            for item in lista_numeros:
                                writer.writerow(item)
                        print("Arquivo utentes.csv criado.")
                except Exception as e:
                    print("Erro ao converter utentes:", e)
            case _:
                print("Opção inválida! Tente novamente.") 

if __name__ == "__main__":
    main()