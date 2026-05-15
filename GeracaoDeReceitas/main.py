from itertools import combinations
from models.utente import Utente
from repository.data_repository import exportar_utentes
from services import utente_service, medicacao_service

def menu_gerar_utentes(lista_utentes: list[Utente]) -> list[Utente]:
    """Gerencia a opção de gerar números de utentes."""
    try:
        qtd = int(input("Número de utentes: "))
        return utente_service.gerar_utentes(qtd)
    except ValueError:
        print("Entrada inválida.")
        return lista_utentes

def menu_atribuir_medicamentos(lista_utentes: list[Utente]):
    """Gerencia a opção de atribuir medicamentos."""
    num_utente = input("Número do utente: ")
    utente = next((u for u in lista_utentes if u.numero_utente == num_utente), None)
    
    if not utente:
        print("Utente não encontrado.")
        return

    try:
        qtd = int(input("Número de medicamentos (3-5): "))
        if 3 <= qtd <= 5:
            utente.medicamentos = medicacao_service.gerar_lista_medicamentos(qtd)
            print(f"Medicamentos atribuídos a {utente.nome}.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu_avaliar_interacoes(lista_utentes: list[Utente], medicamentos: list[str], matriz: list[list[int]]):
    """Gerencia a opção de avaliar interações."""
    num_utente = input("Número do utente: ")
    utente = next((u for u in lista_utentes if u.numero_utente == num_utente), None)
    
    if not utente or not utente.medicamentos:
        print("Utente não encontrado ou sem medicamentos.")
        return

    combos = list(combinations(utente.medicamentos, 2))
    ratings = []
    for med1, med2 in combos:
        r = medicacao_service.buscar_interacao(medicamentos, matriz, med1, med2)
        if r is not None:
            print(f"{med1} + {med2}: {r}")
            ratings.append(r)
    
    if any(r > 0 for r in ratings):
        print("\n>>> NÃO PASSOU (Interação detectada) <<<")
    else:
        print("\n>>> PASSOU <<<")

def main():
    """Função principal."""
    medicamentos, matriz = medicacao_service.gerar_matriz_interacao()
    lista_utentes = []

    while True:
        print(r"""   _____                     /\/|             _                          _ _            
  / ____|                   |/\/             | |                        (_) |           
 | |  __  ___ _ __ __ _  ___ __ _  ___     __| | ___   _ __ ___  ___ ___ _| |_ __ _ ___ 
 | | |_ |/ _ \ '__/ _` |/ __/ _` |/ _ \   / _` |/ _ \ | '__/ _ \/ __/ _ \ | __/ _` / __|
 | |__| |  __/ | | (_| | (_| (_| | (_) | | (_| |  __/ | | |  __/ (_|  __/ | || (_| \__ \
  \_____|\___|_|  \__,_|\___\__,_|\___/   \__,_|\___| |_|  \___|\___\___|_|\__\__,_|___/
                         )_)                                                            
                                                                                        """)
        print("1. Gerar utentes\n2. Atribuir medicamentos\n3. Listar utentes\n4. Ver matriz\n5. Avaliar interações\n6. Exportar\n7. Sair")
        opcao = input("Opção: ")
    
        if opcao == "1":
            lista_utentes = menu_gerar_utentes(lista_utentes)
        elif opcao == "2":
            menu_atribuir_medicamentos(lista_utentes)
        elif opcao == "3":
            for u in lista_utentes: print(u)
        elif opcao == "4":
            for linha in matriz: print(linha)
        elif opcao == "5":
            menu_avaliar_interacoes(lista_utentes, medicamentos, matriz)
        elif opcao == "6":
            exportar_utentes(lista_utentes)
        elif opcao == "7":
            break

if __name__ == "__main__":
    main()
